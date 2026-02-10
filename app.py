from flask import Flask, render_template
import os


app = Flask(__name__)

# Data: Tech Levels & Concepts
levels = [
    {
        "slug": "trainee",
        "name": "Trainee / Becario",
        "badge": "Nivel 0",
        "color": "#94a3b8",  # Gray/Slate
        "years": "0 - 1 año",
        "image": "trainee.png",
        "concepts": [
            {"title": "Lógica de programación básica", "desc": "Entender variables, bucles, condiciones y cómo estructurar instrucciones secuenciales."},
            {"title": "Algoritmos simples", "desc": "Resolver problemas matemáticos o de ordenamiento sencillos paso a paso."},
            {"title": "Conceptos básicos de Git", "desc": "Operaciones fundamentales: clone, add, commit, push y pull para guardar código."},
            {"title": "HTML & CSS básico", "desc": "Estructura de una página web y estilos básicos (colores, fuentes, márgenes)."},
            {"title": "Entender qué es una terminal", "desc": "Navegar carpetas y ejecutar comandos básicos sin interfaz gráfica."},
            {"title": "Ganas de aprender y proactividad", "desc": "Actitud de búsqueda de soluciones y curiosidad constante."}
        ],
        "details": "El punto de partida. Como Trainee, tu foco principal es aprender. Estarás expuesto a tecnologías reales y procesos de desarrollo, absorbiendo conocimiento como una esponja. No se espera que sepas todo, sino que tengas la curiosidad y la disciplina para averiguarlo. Trabajarás bajo supervisión constante y tus tareas estarán bien definidas para evitar bloqueos.",
        "jobs": [
            {"title": "Desarrollador Trainee", "desc": "Aprendiz en equipo de desarrollo, realiza tareas guiadas y capacitación."},
            {"title": "Becario de Sistemas", "desc": "Estudiante aplicando conocimientos académicos en entorno real."},
            {"title": "Pasante de Desarrollo", "desc": "Rol temporal enfocado en ganar primera experiencia laboral."},
            {"title": "Auxiliar de Programación", "desc": "Asiste a desarrolladores senior en tareas rutinarias y documentación."},
            {"title": "Estudiante en Práctica", "desc": "Vinculación universidad-empresa para realizar prácticas profesionales."}
        ]
    },
    {
        "slug": "junior",
        "name": "Junior",
        "badge": "Nivel 1",
        "color": "#4ade80", # Green
        "years": "1 - 3 años",
        "image": "junior.png",
        "concepts": [
            {"title": "Dominio de un lenguaje de programación", "desc": "Escribir código fluido en Python, Java, JS, etc. sin consultar la sintaxis constantemente."},
            {"title": "POO (Programación Orientada a Objetos)", "desc": "Clases, objetos, herencia, polimorfismo y encapsulamiento."},
            {"title": "Git flow básico", "desc": "Manejo de ramas (branches), pull requests y resolución de conflictos básicos."},
            {"title": "Consumo de APIs REST básico", "desc": "Hacer peticiones HTTP (GET, POST) a servicios externos y procesar respuestas JSON."},
            {"title": "Bases de datos relacionales (SQL)", "desc": "Consultas SELECT, INSERT, UPDATE, DELETE y uniones (JOINs) simples."},
            {"title": "Debugging básico", "desc": "Uso de herramientas de depuración para encontrar y corregir errores en el código."},
            {"title": "Uso de frameworks inicial", "desc": "Conocimiento básico de herramientas como React, Flask o Spring Boot."}
        ],
        "details": "Ya puedes aportar valor real al equipo. Un desarrollador Junior puede completar tareas de dificultad baja o media con cierta autonomía, aunque aún requerirá guía en decisiones complejas. Es el momento de consolidar las bases, entender el ciclo de vida del software y empezar a escribir código limpio y mantenible.",
        "jobs": [
            {"title": "Junior Developer", "desc": "Escribe código productivo y soluciona bugs bajo supervisión moderada."},
            {"title": "Desarrollador Web Junior", "desc": "Mantiene y actualiza sitios web o aplicaciones web existentes."},
            {"title": "Analista Programador Junior", "desc": "Analiza requerimientos simples y los traduce en código funcional."},
            {"title": "Backend Developer Jr", "desc": "Trabaja en lógica del servidor y bases de datos con guía senior."},
            {"title": "Frontend Developer Jr", "desc": "Implementa interfaces de usuario siguiendo diseños predefinidos."}
        ]
    },
    {
        "slug": "mid-level",
        "name": "Mid-Level / Semi Senior",
        "badge": "Nivel 2",
        "color": "#38bdf8", # Sky Blue
        "years": "3 - 5 años",
        "image": "mid.png",
        "concepts": [
            {"title": "Patrones de diseño", "desc": "Soluciones reutilizables como Singleton, Factory, Observer o Strategy."},
            {"title": "Principios SOLID", "desc": "Cinco principios clave para escribir código limpio, mantenible y escalable."},
            {"title": "Testing (Unitario, Integración)", "desc": "Escribir pruebas automatizadas para asegurar que el código no se rompa."},
            {"title": "Optimización de SQL", "desc": "Uso de índices, análisis de planes de ejecución y queries eficientes."},
            {"title": "CI/CD pipelines básicos", "desc": "Pipelines de integración y despliegue continuo (GitHub Actions, Jenkins)."},
            {"title": "Docker y contenedores", "desc": "Empaquetar aplicaciones y sus dependencias en contenedores ligeros."},
            {"title": "Refactoring de código legacy", "desc": "Mejorar la estructura interna de código antiguo sin cambiar su comportamiento."},
            {"title": "Mentoring de Juniors", "desc": "Guiar y ayudar a los miembros menos experimentados del equipo."}
        ],
        "details": "El caballo de batalla del equipo. Un Semi Senior es capaz de tomar un requerimiento y llevarlo a producción con mínima supervisión. Entiendes no solo 'cómo' escribir código, sino 'por qué' hacerlo de cierta manera. Empiezas a ver el 'big picture', te preocupas por la calidad, los tests y la deuda técnica.",
        "jobs": [
            {"title": "Software Engineer", "desc": "Rol estándar: diseña, desarrolla y mantiene software de calidad."},
            {"title": "Full Stack Developer", "desc": "Se maneja con soltura tanto en frontend como en backend."},
            {"title": "SSR Developer", "desc": "Desarrollador con autonomía para features completas."},
            {"title": "Analista Desarrollador", "desc": "Fuerte componente de análisis funcional y técnico de soluciones."},
            {"title": "Ingeniero de Software", "desc": "Aplica principios de ingeniería a la construcción de sistemas."}
        ]
    },
    {
        "slug": "senior",
        "name": "Senior",
        "badge": "Nivel 3",
        "color": "#a78bfa", # Purple
        "years": "+5 años",
        "image": "senior.png",
        "concepts": [
            {"title": "Arquitectura de Software", "desc": "Diseño de alto nivel: Hexagonal, Clean Architecture, Event-Driven."},
            {"title": "Sistemas distribuidos", "desc": "Manejo de consistencia eventual, tolerancia a fallos y microservicios."},
            {"title": "Escalabilidad y Performance", "desc": "Caching, balanceo de carga, sharding y optimización de recursos."},
            {"title": "Seguridad (OWASP)", "desc": "Prevención de vulnerabilidades como Inyección SQL, XSS, CSRF."},
            {"title": "Cloud Computing a fondo", "desc": "Arquitecturas serverless, IaaS/PaaS en AWS, Azure o GCP."},
            {"title": "Decisiones técnicas de alto nivel", "desc": "Elegir el stack tecnológico adecuado para problemas complejos."},
            {"title": "Liderazgo técnico", "desc": "Definir estándares, revisar diseños y desbloquear al equipo."},
            {"title": "System Design", "desc": "Diseñar sistemas complejos desde cero considerando todos los requisitos."}
        ],
        "details": "Un referente técnico. El Senior no solo resuelve problemas complejos, sino que evita que ocurran. Su impacto va más allá de su propio código; eleva el nivel de todo el equipo a través de mentoring, code reviews y decisiones arquitectónicas sólidas. Entiende el negocio y cómo la tecnología puede impulsarlo.",
        "jobs": [
            {"title": "Senior Software Engineer", "desc": "Referente técnico, resuelve problemas complejos y diseña sistemas."},
            {"title": "Technical Lead (Hands-on)", "desc": "Lidera equipo técnicamente mientras sigue programando."},
            {"title": "Staff Engineer", "desc": "Rol técnico de alto nivel con impacto en múltiples equipos."},
            {"title": "Expert Developer", "desc": "Especialista profundo en una tecnología o dominio específico."},
            {"title": "Consultor Técnico Senior", "desc": "Asesora sobre mejores prácticas y soluciones a clientes."}
        ]
    },
    {
        "slug": "architect",
        "name": "Tech Lead / Architect",
        "badge": "Nivel 4",
        "color": "#fbbf24", # Amber/Gold
        "years": "+8 años",
        "image": "architect.png",
        "concepts": [
            {"title": "Visión estratégica de tecnología", "desc": "Alinear la tecnología con los objetivos de negocio a largo plazo."},
            {"title": "Arquitectura empresarial", "desc": "Estructura de sistemas a nivel de toda la organización."},
            {"title": "Gestión de deuda técnica", "desc": "Estrategias para pagar intereses técnicos sin frenar el desarrollo."},
            {"title": "Comunicación con stakeholders", "desc": "Traducir problemas técnicos a lenguaje de negocio y viceversa."},
            {"title": "Diseño de alta disponibilidad", "desc": "Sistemas que nunca caen (99.999% uptime), redundancia y disaster recovery."},
            {"title": "Estándares de ingeniería", "desc": "Definir guías de estilo, prácticas y herramientas para toda la empresa."},
            {"title": "Cultura de ingeniería", "desc": "Fomentar la excelencia técnica, el aprendizaje y la colaboración."}
        ],
        "details": "El visionario. El Arquitecto define el esqueleto sobre el que se construye el software. Su responsabilidad es garantizar que el sistema sea escalable, seguro y mantenible a largo plazo. Dialoga con el negocio para traducir necesidades en soluciones técnicas y define los estándares que guiarán a múltiples equipos.",
        "jobs": [
            {"title": "Software Architect", "desc": "Define la estructura y patrones de alto nivel de sistemas complejos."},
            {"title": "Solutions Architect", "desc": "Diseña soluciones tecnológicas para necesidades de negocio específicas."},
            {"title": "Principal Engineer", "desc": "Ingeniero de máxima jerarquía, define estrategia técnica."},
            {"title": "CTO (en startups)", "desc": "Director de tecnología, alinea tech con objetivos de negocio."},
            {"title": "Engineering Manager", "desc": "Gestión de personas y procesos técnicos (pivoteando a management)."},
            {"title": "Tech Lead", "desc": "Lidera equipo técnico, define estándares y vela por la calidad."}
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html', levels=levels)

@app.route('/level/<slug>')
def level_detail(slug):
    level = next((l for l in levels if l['slug'] == slug), None)
    if level:
        return render_template('detail.html', level=level)
    return "Nivel no encontrado", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
