diet_suggestion(diabetes, ['High-fiber foods', 'Whole grains', 'Non-starchy vegetables', 'Lean protein', 'Healthy fats']).
diet_suggestion(hypertension, ['Low-sodium foods', 'Fruits and vegetables', 'Whole grains', 'Lean protein', 'Healthy fats']).
% Define predicate to suggest diet based on disease
suggest_diet(Disease, Diet) :-
    diet_suggestion(Disease, Diet).
