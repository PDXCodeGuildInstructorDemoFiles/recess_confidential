import character


mrs_frizzle = character.NpcEssential(
    'Mrs. Frizzle', 
    'Middle aged science teacher', 
    'interactions_essential', 
    mini_game = trivia.trivia_game,
    genre = 'science',
    inventory=[]
    )

comic_kid = character.NpcEssential(
    'Ned Beasley', 
    'Resident comic-book expert', 
    'interactions_essential', 
    mini_game = trivia.trivia_game,
    genre = 'comics',
    inventory=[]
    )

jeremy = character.NpcEssential(
    'Jeremy', 
    'Tic-Tac-Toe Student', 
    'interactions_essential', 
    mini_game = None, 
    inventory=[]
    )

red_mcguffin = character.NpcEssential(
    'red_mcguffin', 
    'blackjack student Student', 
    'interactions_essential', 
    mini_game = black_jack_func.black_jack, 
    inventory=[]
    )

adam_jacobs = character.NpcNonEssential( 
    'Adam Jacobs', 
    description, 
    'interactions_nonessential'
    )
bryce_balin = character.NpcNonEssential( 
    'Bryce Balin', 
    description, 
    'interactions_nonessential'
    )
becky_barnett = character.NpcNonEssential( 
    'Becky Barnett', 
    description, 
    'interactions_nonessential'
    )
jered_kropholler = character.NpcNonEssential( 
    'Jered Kropholler', 
    description, 
    'interactions_nonessential'
    )
tanner_laramie = character.NpcNonEssential( 
    'Tanner Laramie', 
    description, 
    'interactions_nonessential'
    )
jessica_nathenson = character.NpcNonEssential( 
    'Jessica Nathenson', 
    description, 
    'interactions_nonessential'
    )
judy_wrench = character.NpcNonEssential( 
    'Judy Wrench', 
    description, 
    'interactions_nonessential'
    )
lucy_zastophil = character.NpcNonEssential( 
    'Lucy Zastophil', 
    description, 
    'interactions_nonessential'
    )


