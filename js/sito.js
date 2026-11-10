// Brizzolari — piccoli comportamenti del sito (menu, mappa, modulo contatti)
(function () {
  // Menu mobile
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav-principale');
  if (toggle && nav) {
    var chiudi = function () {
      nav.classList.remove('aperto');
      toggle.setAttribute('aria-expanded', 'false');
    };
    toggle.addEventListener('click', function () {
      var aperto = nav.classList.toggle('aperto');
      toggle.setAttribute('aria-expanded', aperto ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) chiudi(); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('aperto')) { chiudi(); toggle.focus(); }
    });
  }

  // Anno nel footer
  document.querySelectorAll('[data-anno]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Mappa caricata solo su richiesta (niente cookie di terze parti prima del consenso)
  document.querySelectorAll('[data-carica-mappa]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.closest('[data-mappa]');
      var iframe = document.createElement('iframe');
      iframe.src = box.getAttribute('data-mappa');
      iframe.title = 'Mappa: Panificio Pasticceria Brizzolari, Peschiera del Garda';
      iframe.loading = 'lazy';
      iframe.referrerPolicy = 'no-referrer-when-downgrade';
      box.replaceChildren(iframe);
    });
  });

  // Modulo contatti: compone una email pronta da inviare
  var form = document.getElementById('modulo-contatti');
  if (!form) return;
  var motivo = form.elements.motivo;
  var errore = form.querySelector('[data-errore]');
  var aggiornaTorta = function () {
    var torta = motivo.value === 'Torta su ordinazione';
    form.querySelectorAll('[data-solo-torta]').forEach(function (el) { el.hidden = !torta; });
  };
  if (new URLSearchParams(location.search).get('tipo') === 'torta') motivo.value = 'Torta su ordinazione';
  motivo.addEventListener('change', aggiornaTorta);
  aggiornaTorta();

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var mancanti = Array.prototype.filter.call(form.querySelectorAll('[required]'), function (el) {
      return el.type === 'checkbox' ? !el.checked : !el.value.trim();
    });
    form.querySelectorAll('[aria-invalid]').forEach(function (el) { el.removeAttribute('aria-invalid'); });
    if (mancanti.length) {
      mancanti.forEach(function (el) { el.setAttribute('aria-invalid', 'true'); });
      errore.textContent = 'Manca qualcosa: compila i campi obbligatori e accetta l’informativa privacy.';
      errore.hidden = false;
      mancanti[0].focus();
      return;
    }
    errore.hidden = true;
    var f = form.elements;
    var righe = [
      'Richiesta: ' + f.motivo.value,
      'Nome: ' + f.nome.value.trim(),
      'Telefono: ' + f.telefono.value.trim()
    ];
    if (f.email.value.trim()) righe.push('Email: ' + f.email.value.trim());
    if (f.motivo.value === 'Torta su ordinazione' && f.data.value) righe.push('Data di ritiro: ' + f.data.value);
    righe.push('', f.messaggio.value.trim());
    var oggetto = f.motivo.value + ' – ' + f.nome.value.trim();
    location.href = 'mailto:' + form.getAttribute('data-email') +
      '?subject=' + encodeURIComponent(oggetto) + '&body=' + encodeURIComponent(righe.join('\n'));
  });
})();
