// Mock data for crowdfunding cases
// This data simulates the response from /api/v1/crowdfunding/casos/
// and individual case details from /api/v1/crowdfunding/casos/<id>/

export const mockCases = [
  {
    id: 1,
    creador: {
      id_morelia: "CREADOR001",
      nombre_completo: "Maria Elena S.",
      email: "maria@example.com",
    },
    titulo: "Comedor Comunitario 'Esperanza'",
    quien_soy: "Somos un grupo de voluntarios dedicados a proveer alimentos nutritivos a personas de bajos recursos en la colonia Vista Hermosa.",
    que_necesito: "Necesitamos fondos para adquirir utensilios de cocina nuevos, mesas, sillas y cubrir gastos de alimentos no perecederos para los próximos 3 meses.",
    porque: "Nuestro comedor actual tiene equipamiento muy antiguo y insuficiente para la demanda creciente. Con tu ayuda, podemos servir a más personas y ofrecer un espacio más digno.",
    detalles_adicionales: "Realizamos jornadas de alimentación tres veces por semana. También ofrecemos talleres básicos de nutrición.",
    texto_promocional: "¡Ayúdanos a seguir alimentando sonrisas en Vista Hermosa! Cada peso cuenta.",
    video_promocional: "https://www.youtube.com/embed/dQw4w9WgXcQ", // Placeholder YouTube URL
    imagen_promocional: "casos_imagenes/comedor_esperanza.jpg", // Path consistent with Django's upload_to
    categoria: "Comunitario", // Simulates categoria.nombre
    cantidad_requerida: 75000.00,
    cantidad_obtenida: 15250.00,
    estatus: "Activo", // Simulates estatus.nombre
    fecha_publicacion: "2024-07-01",
    fecha_creacion: "2024-06-25T10:00:00Z",
    fecha_fin: "2024-09-30",
    programa_municipal: null, // Simulates programa_municipal.descripcion_nombre
    articulos: [
      { id: 1, descripcion: "Juego de ollas grandes (5 piezas)", recibo_tipo: "Factura/Nota", precio: 3500.00 },
      { id: 2, descripcion: "Compra de 50kg de arroz y frijol", recibo_tipo: "Nota de Venta", precio: 2200.00 },
      { id: 3, descripcion: "5 Mesas plegables", recibo_tipo: "Factura", precio: 7500.00 },
    ]
  },
  {
    id: 2,
    creador: {
      id_morelia: "JUANPZ02",
      nombre_completo: "Juan Pérez L.",
      email: "juan.perez@example.com",
    },
    titulo: "Taller de Robótica para Niños de Morelia",
    quien_soy: "Soy un ingeniero en mecatrónica con pasión por la enseñanza. Quiero acercar la tecnología a los niños de mi comunidad.",
    que_necesito: "Fondos para comprar kits básicos de robótica (Arduino, sensores, motores), laptops reacondicionadas y material didáctico.",
    porque: "La robótica fomenta el pensamiento lógico, la creatividad y prepara a los niños para el futuro. En Morelia hay poco acceso a este tipo de talleres a bajo costo.",
    detalles_adicionales: "El taller se impartiría los sábados por la mañana en un espacio comunitario. Se planea para 20 niños inicialmente.",
    texto_promocional: "¡Impulsa el futuro de Morelia! Apoya nuestro taller de robótica para niños.",
    video_promocional: null,
    imagen_promocional: "casos_imagenes/robotica_ninos.jpg", // Path consistent with Django's upload_to
    categoria: "Educación",
    cantidad_requerida: 40000.00,
    cantidad_obtenida: 22500.00,
    estatus: "Activo",
    fecha_publicacion: "2024-07-15",
    fecha_creacion: "2024-07-01T14:30:00Z",
    fecha_fin: "2024-10-15",
    programa_municipal: "Fomento Educativo STEM",
    articulos: [
      { id: 4, descripcion: "10 Kits Arduino Uno básicos", recibo_tipo: "Factura", precio: 7000.00 },
      { id: 5, descripcion: "5 Laptops reacondicionadas", recibo_tipo: "Factura", precio: 15000.00 },
    ]
  },
  {
    id: 3,
    creador: {
      id_morelia: "ANAGTZ03",
      nombre_completo: "Ana Gutiérrez",
      email: "ana.gtz@example.com",
    },
    titulo: "Refugio Temporal para Animales Callejeros",
    quien_soy: "Amante de los animales y rescatista independiente. Busco mejorar las condiciones de los animales que rescato mientras encuentran un hogar.",
    que_necesito: "Materiales para construir mejores jaulas y áreas de resguardo, alimento medicado, vacunas y apoyo para esterilizaciones.",
    porque: "Muchos animales son abandonados y sufren en las calles. Un refugio temporal digno aumenta sus posibilidades de adopción y bienestar.",
    detalles_adicionales: "Actualmente cuido a 15 perros y 10 gatos en mi propiedad con recursos limitados.",
    texto_promocional: "Dales una segunda oportunidad. Ayuda a construir un refugio digno para animales rescatados.",
    video_promocional: null,
    imagen_promocional: "casos_imagenes/refugio_animales.jpg", // Path consistent with Django's upload_to
    categoria: "Cuidado Animal",
    cantidad_requerida: 90000.00,
    cantidad_obtenida: 12300.00,
    estatus: "Pausado", // Ejemplo de otro estatus
    fecha_publicacion: "2024-06-01",
    fecha_creacion: "2024-05-20T18:00:00Z",
    fecha_fin: "2024-08-30",
    programa_municipal: null,
    articulos: []
  },
  {
    id: 4,
    creador: {
      id_morelia: "ECOART04",
      nombre_completo: "Colectivo EcoArte",
      email: "ecoarte@example.com",
    },
    titulo: "Mural Ecológico en Colonia Obrera",
    quien_soy: "Somos un colectivo de artistas urbanos enfocados en el arte con mensaje ambiental.",
    que_necesito: "Pinturas ecológicas, andamios (renta), brochas, y apoyo para la preparación del muro (limpieza y sellado).",
    porque: "Queremos embellecer un espacio público deteriorado y, al mismo tiempo, generar conciencia sobre la importancia del reciclaje y cuidado del medio ambiente a través del arte.",
    detalles_adicionales: "El mural se realizará en una pared de 20x5 metros cedida por la comunidad. Contará con participación de jóvenes de la colonia.",
    texto_promocional: "Transforma un muro gris en un mensaje de esperanza verde. ¡Apoya el arte urbano con conciencia!",
    video_promocional: null,
    imagen_promocional: "casos_imagenes/mural_ecologico.jpg", // Path consistent with Django's upload_to
    categoria: "Arte y Cultura",
    cantidad_requerida: 25000.00,
    cantidad_obtenida: 25000.00, // Caso fondeado
    estatus: "Completado",
    fecha_publicacion: "2024-05-01",
    fecha_creacion: "2024-04-15T09:00:00Z",
    fecha_fin: "2024-06-15",
    programa_municipal: null,
    articulos: [
      { id: 6, descripcion: "Cubetas de pintura ecológica (varios colores)", recibo_tipo: "Factura", precio: 15000.00 },
      { id: 7, descripcion: "Renta de andamio por 2 semanas", recibo_tipo: "Recibo", precio: 6000.00 },
    ]
  }
];

// Helper para obtener un caso por ID, simulando la respuesta de /casos/<id>/
export function getMockCaseById(id) {
  const caseId = parseInt(id, 10);
  return mockCases.find(c => c.id === caseId) || null;
}

// Mock data for categories (simulates response from a /catalogos/categorias/ endpoint)
export const mockCategories = [
  { id: 1, nombre: 'Salud y Bienestar', descripcion: 'Proyectos relacionados con la salud física y mental.', activo: true },
  { id: 2, nombre: 'Educación', descripcion: 'Iniciativas para mejorar la educación y el aprendizaje.', activo: true },
  { id: 3, nombre: 'Emprendimiento', descripcion: 'Apoyo a nuevos negocios y emprendedores.', activo: true },
  { id: 4, nombre: 'Arte y Cultura', descripcion: 'Fomento a expresiones artísticas y culturales.', activo: true },
  { id: 5, nombre: 'Medio Ambiente', descripcion: 'Proyectos para la conservación y mejora del entorno.', activo: true },
  { id: 6, nombre: 'Comunitario', descripcion: 'Iniciativas para el desarrollo y bienestar de comunidades.', activo: true },
  { id: 7, nombre: 'Cuidado Animal', descripcion: 'Proyectos para el bienestar y protección animal.', activo: true },
  { id: 8, nombre: 'Tecnología', descripcion: 'Desarrollo e implementación de soluciones tecnológicas.', activo: true },
  { id: 9, nombre: 'Deporte', descripcion: 'Fomento a la actividad física y el deporte.', activo: false }, // Ejemplo inactivo
];

// Mock data for user types (simulates /catalogos/tipos_usuario/)
export const mockUserTypes = [
    { id: 1, nombre: 'Ciudadano', activo: true },
    { id: 2, nombre: 'Empresa', activo: true },
    { id: 3, nombre: 'Municipio', activo: true },
    { id: 4, nombre: 'Organización Civil', activo: true },
];

// Mock data for user levels (simulates /catalogos/niveles_usuario/)
export const mockUserLevels = [
    { id: 1, nombre: 'Bronce', color: '#CD7F32', icono_path: 'icons/bronze.png', activo: true },
    { id: 2, nombre: 'Plata', color: '#C0C0C0', icono_path: 'icons/silver.png', activo: true },
    { id: 3, nombre: 'Oro', color: '#FFD700', icono_path: 'icons/gold.png', activo: true },
];

// Mock data for case statuses (simulates /catalogos/estatus_caso/)
export const mockCaseStatuses = [
    { id: 1, nombre: 'En Revisión', activo: true },
    { id: 2, nombre: 'Activo', activo: true },
    { id: 3, nombre: 'Pausado', activo: true },
    { id: 4, nombre: 'Completado', activo: true },
    { id: 5, nombre: 'Cancelado', activo: true },
    { id: 6, nombre: 'No Aprobado', activo: true },
];
