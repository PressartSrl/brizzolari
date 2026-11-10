// Brizzolari — preset Tailwind (v3: presets: [require('./tailwind.preset.js')])
// Con Tailwind v4 usare invece tokens.css + @theme (vedi CLAUDE.md).
module.exports = {
  theme: {
    extend: {
      colors: {
        blu: '#1265A9',
        notte: '#224968',
        crosta: '#E29233',
        oro: '#F5C14C',
        mattone: '#E07D49',
        salvia: '#8ABA8F',
        bruno: '#5E230B',
        caramello: '#9A541F',
        crema: '#FAF2DF',
        farina: '#FFFBF2',
        linea: '#E6D3AE',
      },
      fontFamily: {
        titoli: ['"Baloo 2"', 'system-ui', 'sans-serif'],
        accento: ['Fraunces', 'Georgia', 'serif'],
        testo: ['"DM Sans"', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        display: ['clamp(3rem, 2rem + 4.5vw, 5.5rem)', { lineHeight: '0.92' }],
        h1: ['clamp(2.5rem, 1.8rem + 3vw, 4rem)', { lineHeight: '1' }],
        h2: ['clamp(2rem, 1.5rem + 2vw, 3rem)', { lineHeight: '1' }],
        accento: ['clamp(1.5rem, 1.25rem + 1vw, 2rem)', { lineHeight: '1.2' }],
        etichetta: ['0.8125rem', { lineHeight: '1.2', letterSpacing: '0.14em' }],
      },
      borderRadius: { s: '12px', m: '20px', l: '48px' },
      borderWidth: { DEFAULT: '2px' },
      boxShadow: {
        'adesivo-s': '4px 4px 0 #5E230B',
        'adesivo-m': '6px 6px 0 #5E230B',
        'adesivo-l': '12px 12px 0 #5E230B',
      },
      maxWidth: { contenitore: '1200px' },
    },
  },
};
