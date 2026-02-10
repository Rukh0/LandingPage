const levels = [
    {
        name: "Trainee / Becario",
        badge: "Nivel 0",
        concepts: [
            "Logica de programación básica",
            "Algoritmos simples",
            "Conceptos básicos de Git (clone, pull, commit, push)",
            "HTML & CSS básico",
            "Entender qué es una terminal",
            "Ganas de aprender y proactividad"
        ]
    },
    {
        name: "Junior",
        badge: "Nivel 1",
        concepts: [
            "Dominio de al menos un lenguaje de programación",
            "POO (Programación Orientada a Objetos)",
            "Git flow básico (branches, merge requests)",
            "Consumo de APIs REST básico",
            "Bases de datos relacionales básicas (SQL simple)",
            "Debugging básico",
            "Uso de frameworks (React, Angular, Spring Boot, etc.) a nivel inicial"
        ]
    },
    {
        name: "Mid-Level / Semi Senior",
        badge: "Nivel 2",
        concepts: [
            "Patrones de diseño (Singleton, Factory, Observer)",
            "Principios SOLID",
            "Testing (Unitario, Integración)",
            "Optimización de consultas SQL",
            "CI/CD pipelines básicos",
            "Docker y contenedores",
            "Refactoring de código legacy",
            "Mentoring de Juniors"
        ]
    },
    {
        name: "Senior",
        badge: "Nivel 3",
        concepts: [
            "Arquitectura de Software (Hexagonal, Clean Arch, Microservicios)",
            "Sistemas distribuidos",
            "Escalabilidad y Performance tuning",
            "Seguridad (OWASP)",
            "Cloud Computing a fondo (AWS, Azure, GCP)",
            "Toma de decisiones técnicas de alto nivel",
            "Liderazgo técnico de equipos",
            "System Design"
        ]
    },
    {
        name: "Tech Lead / Architect",
        badge: "Nivel 4",
        concepts: [
            "Visión estratégica de tecnología",
            "Arquitectura empresarial",
            "Gestión de deuda técnica a gran escala",
            "Comunicación con stakeholders no técnicos",
            "Diseño de sistemas de alta disponibilidad y tolerancia a fallos",
            "Definición de estándares de ingeniería",
            "Cultura de ingeniería"
        ]
    }
];

const container = document.getElementById('roadmap-container');

levels.forEach((level, index) => {
    const card = document.createElement('div');
    card.className = 'card';

    const header = document.createElement('div');
    header.className = 'card-header';

    const badge = document.createElement('span');
    badge.className = 'level-badge';
    badge.textContent = level.badge;

    const title = document.createElement('h2');
    title.textContent = level.name;

    header.appendChild(badge);
    header.appendChild(title);

    const list = document.createElement('ul');
    level.concepts.forEach(concept => {
        const item = document.createElement('li');
        item.textContent = concept;
        list.appendChild(item);
    });

    card.appendChild(header);
    card.appendChild(list);

    // Add animation delay based on index for staggered effect
    card.style.animationDelay = `${index * 0.1}s`;

    container.appendChild(card);
});
