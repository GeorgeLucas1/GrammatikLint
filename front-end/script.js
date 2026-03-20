// MODAL DA CORUJA
var owlBtn   = document.getElementById('owl-btn')
var overlay  = document.getElementById('modal-overlay')
var modalClose = document.getElementById('modal-close')

owlBtn.addEventListener('click', function() {
  overlay.classList.add('open')
})
modalClose.addEventListener('click', function() {
  overlay.classList.remove('open')
})
overlay.addEventListener('click', function(e) {
  if (e.target === overlay) overlay.classList.remove('open')
})

// MICROFONE
var btnMic    = document.getElementById('btn-mic')
var micStatus = document.getElementById('mic-status')
var textoEl   = document.getElementById('texto')

var SR = window.SpeechRecognition || window.webkitSpeechRecognition

if (!SR) {
  btnMic.disabled = true
  btnMic.title    = 'Navegador não suporta reconhecimento de voz'
} else {
  var rec       = new SR()
  rec.lang      = 'pt-BR'
  rec.continuous     = false
  rec.interimResults = true
  var listening = false

  btnMic.addEventListener('click', function() {
    if (listening) { rec.stop(); return }
    rec.start()
  })

  rec.onstart = function() {
    listening = true
    btnMic.classList.add('mic-active')
    micStatus.textContent  = '🎙️ Ouvindo... fale agora'
    micStatus.style.display = 'block'
  }

  rec.onresult = function(e) {
    var t = ''
    for (var i = 0; i < e.results.length; i++) t += e.results[i][0].transcript
    textoEl.value = t
    micStatus.textContent = e.results[e.results.length - 1].isFinal
      ? '✅ Fala capturada! Clique em Analisar.'
      : '🎙️ ' + t
  }

  rec.onerror = function(e) {
    var msgs = {
      'not-allowed'  : '⚠️ Permissão de microfone negada.',
      'no-speech'    : '⚠️ Nenhuma fala detectada.',
      'audio-capture': '⚠️ Microfone não encontrado.',
    }
    micStatus.textContent   = msgs[e.error] || '⚠️ Erro: ' + e.error
    micStatus.style.display = 'block'
  }

  rec.onend = function() {
    listening = false
    btnMic.classList.remove('mic-active')
    setTimeout(function() {
      if (!micStatus.textContent.startsWith('✅')) micStatus.style.display = 'none'
    }, 4000)
  }
}

// ANALISADOR
var btn      = document.getElementById('btn')
var btnIcon  = document.getElementById('btn-icon')
var btnText  = document.getElementById('btn-text')
var total    = document.getElementById('total')
var score    = document.getElementById('score')
var erros    = document.getElementById('erros')
var resTitle = document.getElementById('results-title')

function tipoClass(t) {
  var s = (t || '').toLowerCase()
  if (s.indexOf('ortogr')  >= 0) return 'tipo-ortografico'
  if (s.indexOf('gramati') >= 0) return 'tipo-gramatical'
  if (s.indexOf('pontua')  >= 0) return 'tipo-pontuacao'
  if (s.indexOf('estilo')  >= 0) return 'tipo-estilo'
  return ''
}

btn.addEventListener('click', async function() {
  var text = textoEl.value.trim()
  if (!text) return

  btn.disabled        = true
  btnIcon.innerHTML   = '<span class="spinner"></span>'
  btnText.textContent = 'Analisando...'
  erros.innerHTML     = ''
  resTitle.style.display = 'none'
  total.style.display    = 'none'
  score.style.display    = 'none'

  try {
    var res = await fetch('http://localhost:8000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text })
    })
    if (!res.ok) throw new Error()
    var data = await res.json()

    var totalErrors  = data.total_errors != null ? data.total_errors : (data.total || 0)
    var qualityScore = data.quality_score != null ? data.quality_score : (data.score || 0)
    var errorsList   = Array.isArray(data.errors) ? data.errors : []

    total.textContent   = '📝 ' + totalErrors + ' erro(s)'
    total.style.display = 'inline-flex'

    var sc = Number(qualityScore).toFixed(0)
    if (qualityScore >= 70) {
      score.style.cssText = 'display:inline-flex;background:#d1f2eb;color:#1a6645;border:2px solid #2ecc71;padding:0.4rem 1rem;border-radius:20px;font-family:Fredoka One,cursive;font-size:1rem;'
      score.textContent = '⭐ Score: ' + sc
    } else if (qualityScore >= 40) {
      score.style.cssText = 'display:inline-flex;background:#fef9e7;color:#7d6608;border:2px solid #f1c40f;padding:0.4rem 1rem;border-radius:20px;font-family:Fredoka One,cursive;font-size:1rem;'
      score.textContent = '⚡ Score: ' + sc
    } else {
      score.style.cssText = 'display:inline-flex;background:#fde8e8;color:#922b21;border:2px solid #e74c3c;padding:0.4rem 1rem;border-radius:20px;font-family:Fredoka One,cursive;font-size:1rem;'
      score.textContent = '🔴 Score: ' + sc
    }

    resTitle.style.display = 'flex'

    if (errorsList.length > 0) {
      resTitle.textContent = '📋 Erros encontrados:'
      errorsList.forEach(function(erro, i) {
        var tc   = tipoClass(erro.error_type)
        var card = document.createElement('div')
        card.className = 'card ' + tc
        card.style.animationDelay = (i * 0.06) + 's'
        card.innerHTML =
          '<div class="card-header">' +
            '<span class="tipo-tag ' + tc + '">' + (erro.error_type || 'Erro') + '</span>' +
            '<span class="confianca">' + (erro.source || '-') + ' · ' + (((erro.confidence || 0) * 100).toFixed(0)) + '% conf.</span>' +
          '</div>' +
          '<p class="mensagem">' + (erro.message || '') + '</p>' +
          (erro.suggestion ? '<p class="sugestao">💡 Sugestão: ' + erro.suggestion + '</p>' : '')
        erros.appendChild(card)
      })
    } else {
      resTitle.textContent = '🎉 Resultado:'
      erros.innerHTML = '<div class="empty-state">🎉 Parabéns! Nenhum erro encontrado. Ótimo trabalho!</div>'
    }
  } catch (e) {
    resTitle.style.display = 'flex'
    resTitle.textContent   = '⚠️ Resultado:'
    erros.innerHTML = '<div class="error-state">⚠️ Não foi possível conectar ao servidor. Verifique se o backend está rodando.</div>'
  } finally {
    btn.disabled        = false
    btnIcon.textContent = '🔍'
    btnText.textContent = 'Analisar'
  }
})