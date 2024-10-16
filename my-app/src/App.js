import React from 'react';
import './App.css';

const recipes = [
    {
        title: "Chicken Biryani",
        ingredients: [
            "2 cups basmati rice",
            "500 grams chicken, cut into pieces",
            "1 large onion, thinly sliced",
            "2 tomatoes, chopped",
            "1/2 cup plain yogurt",
            "4 tablespoons cooking oil or ghee",
            "2 teaspoons ginger-garlic paste",
            "2-3 green chilies, slit",
            "1/4 cup chopped mint leaves",
            "1/4 cup chopped cilantro",
            "1/2 teaspoon turmeric powder",
            "1 teaspoon red chili powder",
            "1 teaspoon garam masala",
            "Salt, to taste",
            "4 cups water",
            "Whole spices (cloves, cardamom pods, cinnamon)"
        ],
        instructions: [
            "Rinse and soak the basmati rice for 30 minutes, then drain.",
            "Heat oil in a pot, add whole spices, and sauté for a minute.",
            "Add onions and fry until golden brown.",
            "Add ginger-garlic paste and green chilies, sauté for 2 minutes.",
            "Add chicken and cook until white.",
            "Stir in tomatoes, turmeric, red chili powder, and salt; cook until tomatoes soften.",
            "Add yogurt, mint, and cilantro; cook for 5-7 minutes.",
            "Stir in rice gently, then add water and bring to a boil.",
            "Reduce heat, cover, and simmer for 20 minutes.",
            "Fluff with a fork and serve hot."
        ]
    },
    {
        title: "Pasta Primavera",
        ingredients: [
            "200 grams pasta (your choice)",
            "1 bell pepper, chopped",
            "1 zucchini, sliced",
            "1 carrot, julienned",
            "2 tablespoons olive oil",
            "2 cloves garlic, minced",
            "Salt and pepper, to taste",
            "Grated Parmesan cheese (optional)"
        ],
        instructions: [
            "Cook pasta according to package instructions; drain and set aside.",
            "In a pan, heat olive oil and sauté garlic for 1 minute.",
            "Add bell pepper, zucchini, and carrot; cook until tender.",
            "Add cooked pasta, salt, and pepper; toss to combine.",
            "Serve with grated Parmesan cheese, if desired."
        ]
    },
    {
        title: "Chocolate Chip Cookies",
        ingredients: [
            "1 cup unsalted butter, softened",
            "1 cup sugar",
            "1 cup brown sugar",
            "2 eggs",
            "1 teaspoon vanilla extract",
            "3 cups all-purpose flour",
            "1 teaspoon baking soda",
            "1/2 teaspoon salt",
            "2 cups chocolate chips"
        ],
        instructions: [
            "Preheat oven to 350°F (175°C).",
            "In a bowl, cream together butter, sugar, and brown sugar.",
            "Add eggs and vanilla; mix well.",
            "In another bowl, combine flour, baking soda, and salt; gradually mix into wet ingredients.",
            "Stir in chocolate chips.",
            "Drop by tablespoonfuls onto ungreased baking sheets.",
            "Bake for 10-12 minutes or until golden brown."
        ]
    }
];

function Recipe({ recipe }) {
    return (
        <div className="recipe">
            <h2>{recipe.title}</h2>
            <h3>Ingredients</h3>
            <ul>
                {recipe.ingredients.map((ingredient, index) => (
                    <li key={index}>{ingredient}</li>
                ))}
            </ul>
            <h3>Instructions</h3>
            <ol>
                {recipe.instructions.map((step, index) => (
                    <li key={index}>{step}</li>
                ))}
            </ol>
        </div>
    );
}

function App() {
    return (
        <div className="App">
            <h1>Recipe Book</h1>
            {recipes.map((recipe, index) => (
                <Recipe key={index} recipe={recipe} />
            ))}
        </div>
    );
}

export default App;
