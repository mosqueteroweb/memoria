// Datos de configuración y contenido para NeuroActive

var GAME_CONFIG = {
    memoryMatrix: { category: 'Memoria', label: 'Matriz' },
    spatialPath:  { category: 'Memoria', label: 'Ruta' },
    stroop:       { category: 'Atención', label: 'Stroop' },
    goNoGo:       { category: 'Atención', label: 'Semáforo' },
    languageOrder:{ category: 'Lenguaje', label: 'Frases' },
    wordAssoc:    { category: 'Lenguaje', label: 'Asociación' },
    symbolSearch: { category: 'Agilidad Mental', label: 'Símbolos' },
    mathOps:      { category: 'Agilidad Mental', label: 'Operaciones' }
};

var GAME_DATA = {
    stroop: {
        colors: [
            {n:'ROJO', c:'text-red-600'},
            {n:'AZUL', c:'text-blue-600'},
            {n:'VERDE', c:'text-green-600'}
        ]
    },
    languageOrder: {
        phrases: [
            "El cielo es azul",
            "Me gusta el pan",
            "Hoy hace sol",
            "El perro corre",
            "La flor es roja",
            "La luna brilla",
            "El agua moja",
            "Como frutas dulces"
        ]
    },
    wordAssoc: {
        questions: [
            { type: "SINÓNIMO", w: "ALEGRE", opt: ["Triste", "Feliz", "Rápido"], ans: 1 },
            { type: "ANTÓNIMO", w: "CALIENTE", opt: ["Frío", "Fuego", "Tibio"], ans: 0 },
            { type: "SINÓNIMO", w: "AUTO", opt: ["Rueda", "Coche", "Camino"], ans: 1 },
            { type: "ANTÓNIMO", w: "LLENO", opt: ["Vacío", "Todo", "Alto"], ans: 0 },
            { type: "SINÓNIMO", w: "CASA", opt: ["Hogar", "Calle", "Techo"], ans: 0 }
        ]
    },
    symbolSearch: {
        symbols: ['★', '●', '■', '▲', '♦', '♥', '♣', '♠']
    }
};

// Asegurar disponibilidad global
window.GAME_CONFIG = GAME_CONFIG;
window.GAME_DATA = GAME_DATA;
