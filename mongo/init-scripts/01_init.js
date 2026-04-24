// ============================================================
//  Initialisation MongoDB — blog_db avec validation de schéma
//  5 posts requis pour le healthcheck métier
// ============================================================

const db = db.getSiblingDB("blog_db");

// Création de la collection avec validation de schéma JSON
db.createCollection("posts", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["title", "content", "author", "createdAt"],
      properties: {
        title: {
          bsonType: "string",
          description: "Titre de l'article — obligatoire"
        },
        content: {
          bsonType: "string",
          description: "Contenu de l'article — obligatoire"
        },
        author: {
          bsonType: "string",
          description: "Auteur — obligatoire"
        },
        createdAt: {
          bsonType: "date",
          description: "Date de création — obligatoire"
        }
      }
    }
  },
  validationLevel: "strict",
  validationAction: "error"
});

// Insertion des 5 articles initiaux
db.posts.insertMany([
  {
    title: "Introduction à Docker",
    content: "Docker est une plateforme open-source de conteneurisation qui permet d'empaqueter une application et ses dépendances dans un conteneur isolé.",
    author: "Alice Martin",
    createdAt: new Date("2024-01-10T09:00:00Z")
  },
  {
    title: "Docker Compose en pratique",
    content: "Docker Compose simplifie l'orchestration de plusieurs conteneurs via un fichier YAML déclaratif. Idéal pour les environnements de développement et de staging.",
    author: "Bob Dupont",
    createdAt: new Date("2024-01-15T10:30:00Z")
  },
  {
    title: "MongoDB avec Python",
    content: "PyMongo et Motor sont les deux drivers Python pour MongoDB. Motor est la version asynchrone, parfaite pour des frameworks comme FastAPI.",
    author: "Charlie Bernard",
    createdAt: new Date("2024-02-01T08:00:00Z")
  },
  {
    title: "FastAPI : le guide complet",
    content: "FastAPI est un framework web Python moderne et performant, basé sur les annotations de type Python 3.6+. Il génère automatiquement la documentation OpenAPI.",
    author: "Diana Lemaire",
    createdAt: new Date("2024-02-20T14:00:00Z")
  },
  {
    title: "Sécurité des conteneurs",
    content: "Appliquer le principe du moindre privilège dans Docker passe par l'utilisation d'images non-root, des capabilities restreintes et des images minimales (distroless).",
    author: "Eve Rousseau",
    createdAt: new Date("2024-03-05T11:00:00Z")
  }
]);

print("blog_db initialisée : " + db.posts.countDocuments() + " posts insérés.");
