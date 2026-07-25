import json
import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PUZZLES_DIR = BASE_DIR / "puzzles"

NEW_CATEGORIES = [
    "cipher",
    "riddles",
    "logic",
    "timeline",
    "hidden_messages",
    "code_breaking",
    "witness_statements",
    "evidence_analysis"
]

def prepare_directories():
    if PUZZLES_DIR.exists():
        for item in PUZZLES_DIR.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    for cat in NEW_CATEGORIES:
        (PUZZLES_DIR / cat).mkdir(parents=True, exist_ok=True)
    print("Cleaned old puzzle categories and initialized 8 new folders.")

all_puzzles = []

# ==============================================================================
# 1. CIPHER (15 Puzzles)
# ==============================================================================
all_puzzles.extend([
    {
        "id": "cipher_001",
        "title": "The Cipher of Lord Blackwood",
        "category": "cipher",
        "difficulty": "easy",
        "description": "A coded page was recovered from Lord Blackwood's study desk.\nThe message appears encrypted using a Caesar shift of +3.",
        "question": "Decrypt the message:\n\nPHHW PH DW PLGQLJKW",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["MEET ME AT MIDNIGHT", "meet me at midnight", "Meet Me At Midnight"],
        "hints": [
            "The letters appear consistently shifted by the same alphabet offset.",
            "Try moving each letter backward by 3 positions in the alphabet.",
            "P minus 3 positions is M, H minus 3 is E, W minus 3 is T."
        ],
        "solution_explanation": "Shift each letter backward by 3 positions in the alphabet (P->M, H->E, H->E, W->T). Decoded phrase: MEET ME AT MIDNIGHT.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "cipher_002",
        "title": "The Intercepted ROT13 Telegram",
        "category": "cipher",
        "difficulty": "easy",
        "description": "An anonymous telegram was delivered to Scotland Yard.\nThe text was encoded using ROT13 cipher substitution.",
        "question": "Decode the text:\n\nGUR CBVFBS VF VA GUR JVAR",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["THE POISON IS IN THE WINE", "the poison is in the wine"],
        "hints": [
            "ROT13 shifts every letter by exactly 13 places in the alphabet.",
            "G shifted by 13 positions becomes T, U becomes H, R becomes E.",
            "Replace each letter with its alphabet midpoint twin to read the warning."
        ],
        "solution_explanation": "Applying ROT13 (shifting by 13 letters) to 'GUR CBVFBS VF VA GUR JVAR' yields 'THE POISON IS IN THE WINE'.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "cipher_003",
        "title": "The Scullery Mirror Note",
        "category": "cipher",
        "difficulty": "easy",
        "description": "A charred scrap of paper was retrieved from the kitchen fireplace.\nThe message was written entirely in reverse order.",
        "question": "Read the hidden phrase:\n\nRETSAM EHT SILLIK RELTUB EHT",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["THE BUTLER KILLS THE MASTER", "the butler kills the master"],
        "hints": [
            "The words are written completely backward.",
            "Start reading from the very last letter of the last word.",
            "Reverse each word: RETSAM -> MASTER, EHT -> THE, SILLIK -> KILLS, RELTUB -> BUTLER, EHT -> THE."
        ],
        "solution_explanation": "Reading the words backwards from right to left reveals: 'THE BUTLER KILLS THE MASTER'.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "cipher_004",
        "title": "The Telegrapher's Morse Code",
        "category": "cipher",
        "difficulty": "easy",
        "description": "A radio transmission tape was recovered near the telegraph desk.\nThe dots and dashes represent standard international Morse code.",
        "question": "Decode this Morse code string (slashes separate words):\n\n- .... . / ... .- ..-. . / .. ... / -... . .... .. -. -.. / - .... . / --. .-. .. -..",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["THE SAFE IS BEHIND THE GRID", "the safe is behind the grid"],
        "hints": [
            "Standard international Morse code is used.",
            "-... is B, . is E, .... is H, .. is I, -. is N, -.. is D.",
            "Translate each letter sequence: -.... = THE, ... .- ..-. . = SAFE, .. ... = IS, -... . .... .. -. -.. = BEHIND, - .... . = THE, --. .-. .. -.. = GRID."
        ],
        "solution_explanation": "Translating each Morse code character (-.... = THE, ... .- ..-. . = SAFE, .. ... = IS, -... . .... .. -. -.. = BEHIND, - .... . = THE, --. .-. .. -.. = GRID) reveals 'THE SAFE IS BEHIND THE GRID'.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "cipher_005",
        "title": "The Parlor Shift Note",
        "category": "cipher",
        "difficulty": "easy",
        "description": "A slip of parchment was discovered hidden under a parlor sofa cushion.\nThe text was encoded using a Caesar shift of +2.",
        "question": "Decrypt this message shifted by +2:\n\nRFC NCKCJ GQ GL RFC TCYUR",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["THE JEWEL IS IN THE VAULT", "the jewel is in the vault"],
        "hints": [
            "Each letter has been shifted forward by 2 positions.",
            "To decrypt, move each letter backward by 2 steps in the alphabet.",
            "Shift backward: R - 2 = T? No, T - 2 = R, H - 2 = F, E - 2 = C, so RFC represents THE."
        ],
        "solution_explanation": "Moving each letter backward by 2 positions in the alphabet (R->T, F->H, C->E) reveals: 'THE JEWEL IS IN THE VAULT'.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "cipher_006",
        "title": "The Velvet Keyword Cipher",
        "category": "cipher",
        "difficulty": "medium",
        "description": "An encrypted document was found inside a sealed velvet pouch.\nIt uses a keyword substitution cipher based on the keyword 'VELVET'.",
        "question": "Decrypt the message encoded with key 'VELVET':\n\nTBX TFEP HQ WBLTH",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["THE DEED IS VALID", "the deed is valid"],
        "hints": [
            "A keyword cipher removes duplicate letters from the keyword and appends the remaining alphabet.",
            "Keyword VELVET gives unique key header V-E-L-T.",
            "Map each cipher letter back to its standard A-Z counterpart to reveal the phrase."
        ],
        "solution_explanation": "Reversing the keyword substitution mapping ('VELVET' alphabet shift) reveals the underlying secret phrase: 'THE DEED IS VALID'.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "cipher_007",
        "title": "The Mixed Alphabet Alibi",
        "category": "cipher",
        "difficulty": "medium",
        "description": "An encrypted alibi note was recovered from Evidence Folder #7.\nThe note uses the ancient Atbash substitution cipher (A=Z, B=Y, C=X).",
        "question": "Decode this Atbash cipher:\n\nGSV ERXGRN DZH KLISLMVW",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["THE VICTIM WAS POISONED", "the victim was poisoned"],
        "hints": [
            "Atbash flips the alphabet completely: A becomes Z, B becomes Y, C becomes X.",
            "G maps to T, S maps to H, V maps to E.",
            "Translate each letter with its opposite twin from the reverse alphabet."
        ],
        "solution_explanation": "Applying Atbash reverse-alphabet substitution (G->T, S->H, V->E...) yields 'THE VICTIM WAS POISONED'.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "cipher_008",
        "title": "The Conservatory Shift (-5)",
        "category": "cipher",
        "difficulty": "medium",
        "description": "An anonymous letter was recovered from the victim's coat pocket.\nThe letters were shifted backward by 5 positions.",
        "question": "Decrypt this message:\n\nYMJ BIFUMX NX NSIYMJ XIFI",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["THE WEAPON IS IN THE SAFE", "the weapon is in the safe"],
        "hints": [
            "Each letter was shifted backward by 5 positions.",
            "To restore the original text, shift each letter forward by 5 positions.",
            "Y + 5 = T, M + 5 = H, J + 5 = E."
        ],
        "solution_explanation": "Shifting each letter forward by 5 steps (Y->T, M->H, J->E) produces: 'THE WEAPON IS IN THE SAFE'.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "cipher_009",
        "title": "The Clockmaker's Book Cipher",
        "category": "cipher",
        "difficulty": "medium",
        "description": "A notebook page listed numerical references: '1-1-1 2-1-2'.\nFound beside the book with pages:\nLine 1: BEWARE ALL TRAITORS\nLine 2: THE COUSIN FLEES\nLine 3: IN NIGHT FALL",
        "question": "Translate the code 1-1-1 (Line 1, Word 1) 2-1-2 (Line 2, Word 2) to identify the target:",
        "acceptable_answer_format": "Type the decoded phrase.\n\nExample:\nTHE KEY",
        "accepted_answers": ["BEWARE COUSIN", "beware cousin"],
        "hints": [
            "Book ciphers use pairs or triplets: Line Number - Word Number.",
            "Line 1, Word 1 is 'BEWARE'.",
            "Line 2, Word 2 is 'COUSIN'."
        ],
        "solution_explanation": "Lookup 1-1-1 gives 'BEWARE' from Line 1, and 2-1-2 gives 'COUSIN' from Line 2. Combined phrase: BEWARE COUSIN.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "cipher_010",
        "title": "The Letter Shift Matrix",
        "category": "cipher",
        "difficulty": "medium",
        "description": "A cipher slip was recovered from a locked filing cabinet.\nThe encryption alternates between +1 and -1 shifts.",
        "question": "Decrypt 'U G F R F U' (odd positions +1, even positions -1):",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nSECRET",
        "accepted_answers": ["SECRET", "secret"],
        "hints": [
            "Odd letter positions (1st, 3rd, 5th) were shifted +1.",
            "Even letter positions (2nd, 4th, 6th) were shifted -1.",
            "Reverse shifts: 1st letter U (-1) -> T? S (+1)->T. For U -> S! G (+1) -> H? G (+1) -> H -> E! So SECRET."
        ],
        "solution_explanation": "Reversing the alternating shift (+1 on odd positions, -1 on even positions) on 'U G F R F U' yields 'SECRET'.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "cipher_011",
        "title": "The Vigenère Cryptogram",
        "category": "cipher",
        "difficulty": "hard",
        "description": "An encrypted USB drive contained a Vigenère cipher file.\nThe key used for encryption is 'KEY'.",
        "question": "Decrypt the cipher text 'DLI' using keyword 'KEY':",
        "acceptable_answer_format": "Type the decoded word.\n\nExample:\nACT",
        "accepted_answers": ["ACT", "act"],
        "hints": [
            "Vigenère cipher adds key values to plaintext values.",
            "Key values: K=10, E=4, Y=24.",
            "Subtract key value from cipher text letter modulo 26."
        ],
        "solution_explanation": "Subtracting the key values of 'KEY' (K=10, E=4, Y=24) modulo 26 from cipher text 'DLI' yields 'ACT'.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "cipher_012",
        "title": "The Rail Fence Cipher",
        "category": "cipher",
        "difficulty": "hard",
        "description": "An anonymous letter was written on a zig-zag paper strip across 2 rails.\nThe text must be reconstructed by interleaving the rails.",
        "question": "Decrypt the 2-rail fence cipher text:\n\nHESFEISPEN TEAIOPN",
        "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
        "accepted_answers": ["THE SAFE IS OPEN", "the safe is open"],
        "hints": [
            "Rail fence cipher splits text into top and bottom rows alternating.",
            "Top rail contains letters: T E S F E I S P E N",
            "Bottom rail contains letters: H A E O N. Interleave characters from top and bottom."
        ],
        "solution_explanation": "Interleaving the characters from top rail ('T E S F E I S P E N') and bottom rail ('H A E O N') reconstructs 'THE SAFE IS OPEN'.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "cipher_013",
        "title": "The Simple Substitution Key",
        "category": "cipher",
        "difficulty": "hard",
        "description": "Forensic Report #104 contains a simple substitution key:\nE=X, T=Z, H=Y, O=W, R=V, N=U.",
        "question": "Decode the message:\n\nZYX WUZV",
        "acceptable_answer_format": "Type the decoded phrase.\n\nExample:\nTHE ONE",
        "accepted_answers": ["THE ONE", "the one"],
        "hints": [
            "Use the substitution table directly.",
            "Z -> T, Y -> H, X -> E.",
            "W -> O, U -> N, V -> R (wait: ZYX=THE, WUZV=ONE)."
        ],
        "solution_explanation": "Substituting characters according to the key (Z->T, Y->H, X->E, W->O, U->N, V->E) yields 'THE ONE'.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "cipher_014",
        "title": "The Columnar Transposition",
        "category": "cipher",
        "difficulty": "hard",
        "description": "Evidence Folder #7 contained a 3-column transposition cipher.\nColumns read: Col 1: 'TSN', Col 2: 'HIO', Col 3: 'EEN'.",
        "question": "Reconstruct row-by-row (Row 1: T-H-E, Row 2: S-I-G, Row 3: N):",
        "acceptable_answer_format": "Type the decoded phrase.\n\nExample:\nTHE SIGN",
        "accepted_answers": ["THE SIGN", "the sign"],
        "hints": [
            "Read characters across rows from Column 1, Column 2, Column 3.",
            "Row 1: T H E -> THE.",
            "Row 2: S I G -> SIG... Row 3: N."
        ],
        "solution_explanation": "Reading row by row across the 3 columns (Row 1: T-H-E, Row 2: S-I-G, Row 3: N) produces 'THE SIGN'.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "cipher_015",
        "title": "The Polybius Square Grid",
        "category": "cipher",
        "difficulty": "hard",
        "description": "A notebook page contained a 5x5 Polybius Square grid:\nRow 1: A-E, Row 2: F-K, Row 3: L-P, Row 4: Q-U, Row 5: V-Z.",
        "question": "Decode coordinates '44 23 15' (Row-Column):",
        "acceptable_answer_format": "Type the decoded word.\n\nExample:\nTHE",
        "accepted_answers": ["THE", "the"],
        "hints": [
            "Each number pair represents (Row, Column) in the grid.",
            "Row 4, Col 4 is T.",
            "Row 2, Col 3 is H, Row 1, Col 5 is E."
        ],
        "solution_explanation": "Looking up grid coordinates (Row 4 Col 4 = T, Row 2 Col 3 = H, Row 1 Col 5 = E) produces the word 'THE'.",
        "time_limit": 450,
        "reward_points": 300
    }
])

# ==============================================================================
# 2. RIDDLES (15 Puzzles)
# ==============================================================================
all_puzzles.extend([
    {
        "id": "riddles_001",
        "title": "The Wet Floor in the Sealed Study",
        "category": "riddles",
        "difficulty": "easy",
        "description": "A locked study contains a victim lying dead on the floor.\nThe door is locked from the inside, the windows are sealed, and the floor is covered in clear water. No weapon is found.",
        "question": "What weapon was used to kill the victim?",
        "acceptable_answer_format": "Type the object.\n\nExample:\nA painting",
        "accepted_answers": ["Ice Dagger", "ice dagger", "ICE DAGGER", "Ice dagger", "Ice", "ice", "An ice dagger", "an ice dagger"],
        "hints": [
            "Consider weapons that leave no solid trace behind at room temperature.",
            "The pool of water on the floor is the melted remains of the weapon.",
            "An icicle or weapon made of frozen water melted after inflicting the fatal wound."
        ],
        "solution_explanation": "The killer used an ice dagger. After the victim was stabbed, the ice melted into a pool of water at room temperature, leaving no weapon behind.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "riddles_002",
        "title": "The Broken Pocket Watch",
        "category": "riddles",
        "difficulty": "easy",
        "description": "The victim was thrown from the manor balcony into the river below.\nWhen recovered, his pocket watch had stopped completely due to water impact at 10:15.",
        "question": "At what exact time did the victim hit the water?",
        "acceptable_answer_format": "Type the time.\n\nExample:\n10:15 PM",
        "accepted_answers": ["10:15 PM", "10:15 pm", "10:15PM", "10:15", "10:15 P.M."],
        "hints": [
            "The watch mechanism broke instantly upon violent contact with the water.",
            "Look at the hands of the stopped timepiece.",
            "The time displayed on the hands is the exact moment of impact: 10:15."
        ],
        "solution_explanation": "The violent impact of hitting the water instantly stopped the mechanical movement of the pocket watch, freezing the hands at 10:15 PM.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "riddles_003",
        "title": "The Unopened Package in the Field",
        "category": "riddles",
        "difficulty": "easy",
        "description": "A man is found dead in the middle of a deserted field with no tracks near him.\nNext to him lies an unopened package strapped tightly to his back.",
        "question": "What was inside the unopened package?",
        "acceptable_answer_format": "Type the object.\n\nExample:\nA parachute",
        "accepted_answers": ["Parachute", "parachute", "PARACHUTE", "A parachute", "a parachute"],
        "hints": [
            "He arrived in the field from high above.",
            "His life depended on opening that package before reaching the ground.",
            "It was a parachute that failed to open during a jump."
        ],
        "solution_explanation": "The man jumped from an aircraft, but his parachute failed to open, causing his fatal impact in the middle of the field.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "riddles_004",
        "title": "The Staged Suicide",
        "category": "riddles",
        "difficulty": "easy",
        "description": "Lord Vance was found dead at his desk with a gunshot wound to his right temple.\nThe revolver was clutched tightly in his left hand, but gunpowder residue was only on his right cheek.",
        "question": "Was this suicide or murder?",
        "acceptable_answer_format": "Type Murder or Suicide.\n\nExample:\nMurder",
        "accepted_answers": ["Murder", "murder", "MURDER", "It was murder", "Staged murder"],
        "hints": [
            "A left-handed shooter would have gunpowder residue on their left hand.",
            "The wound location and hand holding the gun do not match.",
            "The killer placed the gun in the victim's left hand after shooting him from the right."
        ],
        "solution_explanation": "Gunpowder residue was found on the victim's right cheek from a shot fired from the right, but the gun was found in his left hand. The killer placed the gun in his left hand after shooting him.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "riddles_005",
        "title": "The Mirror Image Alibi",
        "category": "riddles",
        "difficulty": "easy",
        "description": "A witness swears he saw the killer shoot the victim with his left hand while looking in a large parlor mirror.",
        "question": "Which hand did the killer actually use to pull the trigger?",
        "acceptable_answer_format": "Type Right Hand or Left Hand.\n\nExample:\nRight Hand",
        "accepted_answers": ["Right Hand", "right hand", "RIGHT HAND", "Right", "right", "His right hand"],
        "hints": [
            "Mirrors reverse left and right orientations.",
            "If an action appears left-handed in a mirror reflection, what hand is actually moving?",
            "A right hand raising a pistol appears as a left hand in a mirror image."
        ],
        "solution_explanation": "Mirrors reverse lateral orientation. A person raising their right hand appears to raise their left hand in a mirror reflection.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "riddles_006",
        "title": "The Footprints in the Snow",
        "category": "riddles",
        "difficulty": "medium",
        "description": "Fresh snow fell at midnight. Footprints lead straight FROM the victim's cabin TO the town, but NO footprints lead toward the cabin.\nYet the suspect was inside the cabin at 1 AM.",
        "question": "How did the suspect reach the cabin without leaving incoming footprints?",
        "acceptable_answer_format": "Type the action.\n\nExample:\nWalked backward",
        "accepted_answers": ["Walked backward", "walked backward", "WALKED BACKWARD", "Walking backward", "He walked backward", "Walked backwards", "walked backwards"],
        "hints": [
            "He walked to the cabin before or during the snowfall, or altered how he walked.",
            "Think about the direction the boot prints face.",
            "He walked toward the cabin while stepping backward, making it look like someone walked away."
        ],
        "solution_explanation": "The suspect walked to the cabin while facing away and stepping backward, making his incoming footprints point toward the town.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "riddles_007",
        "title": "The Dumbwaiter Scream",
        "category": "riddles",
        "difficulty": "medium",
        "description": "The mansion's vault room is completely soundproofed with heavy lead lining.\nYet a servant heard the victim's scream clearly in the scullery 2 floors down.",
        "question": "Through what channel did the sound travel?",
        "acceptable_answer_format": "Type the channel or opening.\n\nExample:\nDumbwaiter shaft",
        "accepted_answers": ["Dumbwaiter shaft", "dumbwaiter shaft", "DUMBWAITER SHAFT", "Dumbwaiter", "dumbwaiter", "The dumbwaiter shaft"],
        "hints": [
            "Soundproof walls block room sound, but small physical shafts bypass the insulation.",
            "Food and dishes were moved between floors using a mechanical lift shaft.",
            "The open dumbwaiter shaft carried the audio directly to the scullery."
        ],
        "solution_explanation": "The open dumbwaiter shaft passed through the floors, creating an acoustic conduit that carried the sound of the scream into the scullery.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "riddles_008",
        "title": "The Poisoned Wine Ice Cubes",
        "category": "riddles",
        "difficulty": "medium",
        "description": "Two men drank wine poured from the exact same carafe.\nMan A drank his glass fast in 10 seconds and lived. Man B sipped his glass slowly over 20 minutes and died of poison.",
        "question": "Where was the poison hidden?",
        "acceptable_answer_format": "Type the location.\n\nExample:\nIce cubes",
        "accepted_answers": ["Ice cubes", "ice cubes", "ICE CUBES", "The ice cubes", "Ice", "ice"],
        "hints": [
            "The wine itself in the carafe was harmless.",
            "Man A drank quickly before something in the glass could change.",
            "The poison was frozen inside the ice cubes; drinking fast meant the ice hadn't melted yet."
        ],
        "solution_explanation": "The poison was frozen inside the ice cubes. Man A drank quickly before the ice melted, while Man B drank slowly as the poison melted into his glass.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "riddles_009",
        "title": "The Locked Carriage Mystery",
        "category": "riddles",
        "difficulty": "medium",
        "description": "The victim was found dead inside a horse-drawn carriage.\nBoth doors were locked with iron deadbolts from the inside. The key was found on the outside road.",
        "question": "What object did the killer use from outside to move the iron key back out through the window gap?",
        "acceptable_answer_format": "Type the tool.\n\nExample:\nA magnet",
        "accepted_answers": ["Magnet", "magnet", "MAGNET", "A magnet", "a magnet"],
        "hints": [
            "The iron key was pulled across the carriage floor toward the window gap.",
            "No string or thread was left on the key.",
            "A powerful magnetic force dragged the iron key through the gap from the outside."
        ],
        "solution_explanation": "The killer used a strong magnet from outside the carriage window to attract and slide the iron deadbolt key across the floor and out through the narrow gap.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "riddles_010",
        "title": "The Half-Burned Candle Draft",
        "category": "riddles",
        "difficulty": "medium",
        "description": "In a room with no open windows, a candle burned down twice as fast as an identical candle in the hallway.",
        "question": "What secret room feature caused the increased air oxygen flow?",
        "acceptable_answer_format": "Type the room feature.\n\nExample:\nSecret passage",
        "accepted_answers": ["Secret passage", "secret passage", "SECRET PASSAGE", "Secret door", "A secret passage"],
        "hints": [
            "Increased airflow burns candles much faster.",
            "Air was circulating into the room from behind a wall fixture.",
            "A hidden door or secret passage created a strong draft."
        ],
        "solution_explanation": "An unsealed secret passage behind the bookcase created a continuous air draft that supplied extra oxygen, causing the candle to burn twice as fast.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "riddles_011",
        "title": "The Telegram From Beyond",
        "category": "riddles",
        "difficulty": "hard",
        "description": "A suspect died at 9:00 PM in a mountain hut.\nYet a telegram signed with his private code was dispatched from the central office at 10:00 PM.",
        "question": "How did his telegram get sent after his death?",
        "acceptable_answer_format": "Type how it was sent.\n\nExample:\nPre-scheduled",
        "accepted_answers": ["Pre-scheduled", "pre-scheduled", "PRE-SCHEDULED", "Prescheduled", "prescheduled", "Scheduled in advance", "Pre scheduled"],
        "hints": [
            "The suspect didn't send it at 10:00 PM personally.",
            "He arranged the delivery before his demise.",
            "He scheduled a delayed automatic dispatch with the telegraph clerk earlier in the day."
        ],
        "solution_explanation": "The suspect arranged and pre-scheduled the telegram dispatch with the telegraph clerk earlier in the afternoon before he died.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "riddles_012",
        "title": "The Uncut Novel Pages",
        "category": "riddles",
        "difficulty": "hard",
        "description": "The suspect claimed he sat in the library for 3 hours reading the victim's rare new antique book from cover to cover.",
        "question": "What physical feature of 19th-century unread books proved he was lying?",
        "acceptable_answer_format": "Type the book feature.\n\nExample:\nUncut pages",
        "accepted_answers": ["Uncut pages", "uncut pages", "UNCUT PAGES", "The pages were uncut", "Uncut book pages"],
        "hints": [
            "19th-century printed books required a paper knife to open folded sheet edges.",
            "The detective inspected the top edges of the book's pages.",
            "The paper edges were still joined together and uncut, making reading impossible."
        ],
        "solution_explanation": "In the 19th century, untrimmed book leaves required a paper knife to separate. The book's folded top edges were completely uncut, proving it had never been opened.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "riddles_013",
        "title": "The Sealed Vault Oxygen",
        "category": "riddles",
        "difficulty": "hard",
        "description": "Two men were locked inside an airtight steel safe for 8 hours.\nWhen opened, one man was alive and healthy, but the other had suffocated from lack of oxygen.",
        "question": "Why did one man suffocate while the other survived?",
        "acceptable_answer_format": "Type the reason.\n\nExample:\nOne was already dead",
        "accepted_answers": ["One was already dead", "one was already dead", "ONE WAS ALREADY DEAD", "One man was dead", "He was already dead"],
        "hints": [
            "They didn't share the oxygen equally.",
            "One person was not breathing when they were locked inside.",
            "The victim was already a corpse before the vault door closed."
        ],
        "solution_explanation": "One of the two men was already dead before the vault was sealed. Since a corpse does not consume oxygen, the living survivor had enough oxygen to last 8 hours.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "riddles_014",
        "title": "The Single Bullet Chandelier Drop",
        "category": "riddles",
        "difficulty": "hard",
        "description": "A single gunshot killed Victim A standing near the entrance and Victim B standing 20 feet away at the head table.",
        "question": "What heavy ceiling object did the bullet strike to cause Victim B's death?",
        "acceptable_answer_format": "Type the object.\n\nExample:\nChandelier",
        "accepted_answers": ["Chandelier", "chandelier", "CHANDELIER", "The chandelier", "A chandelier"],
        "hints": [
            "The bullet didn't hit Victim B directly.",
            "The bullet severed a holding chain above Victim B.",
            "The shot severed the heavy iron chain supporting the crystal chandelier."
        ],
        "solution_explanation": "The bullet struck the hanging iron chain supporting the heavy ceiling chandelier, causing it to fall directly onto Victim B.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "riddles_015",
        "title": "The Portrait's Eye Peepholes",
        "category": "riddles",
        "difficulty": "hard",
        "description": "The killer spied on the secret meeting in the gallery through a portrait on the wall without cutting new holes in the canvas.",
        "question": "Where were the original hidden openings located in the portrait?",
        "acceptable_answer_format": "Type the location on the portrait.\n\nExample:\nEyes",
        "accepted_answers": ["Eyes", "eyes", "EYES", "The eyes", "Portrait eyes", "Eye holes"],
        "hints": [
            "The artist included dark circular details in the subject's face.",
            "Look at the pupils of the painted figure.",
            "The eye pupils of the painting had been hollowed out from behind."
        ],
        "solution_explanation": "The eye pupils of the portrait were hollowed out from behind, allowing an observer standing in the secret corridor behind the wall to watch the gallery.",
        "time_limit": 450,
        "reward_points": 300
    }
])

# ==============================================================================
# 3. LOGIC DEDUCTION (15 Puzzles)
# ==============================================================================
all_puzzles.extend([
    {
        "id": "logic_001",
        "title": "Three Suspects and One Liar",
        "category": "logic",
        "difficulty": "easy",
        "description": "Three suspects gave depositions after the theft:\nAlice says: 'Bob was in the kitchen.'\nBob says: 'Charlie never left the study.'\nCharlie says: 'Alice is lying.'\nDetective note: Exactly ONE person is lying.",
        "question": "Who is lying?",
        "acceptable_answer_format": "Type only the suspect's name.\n\nExample:\nAlice",
        "accepted_answers": ["Charlie", "charlie", "CHARLIE"],
        "hints": [
            "If Charlie is telling the truth, then Alice must be lying.",
            "If Alice lies, then Bob wasn't in the kitchen, but Bob's statement would need to be evaluated.",
            "Test Charlie being the liar: Alice is telling the truth, Bob is telling the truth. Everything remains consistent!"
        ],
        "solution_explanation": "If Charlie is lying, then Alice and Bob are both telling the truth. Alice says Bob was in the kitchen (True), and Bob says Charlie never left the study (True). This maintains consistency with exactly one liar.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "logic_002",
        "title": "The Room Placement Grid",
        "category": "logic",
        "difficulty": "easy",
        "description": "The Maid, Butler, and Chef were in separate rooms (Library, Kitchen, Study).\n1. The Maid was in the Library.\n2. The Chef was NOT in the Kitchen.",
        "question": "In which room was the Butler?",
        "acceptable_answer_format": "Type only the room name.\n\nExample:\nKitchen",
        "accepted_answers": ["Kitchen", "kitchen", "KITCHEN", "The Kitchen", "the kitchen"],
        "hints": [
            "The Maid occupies the Library.",
            "The Chef cannot be in the Library (Maid is there) or the Kitchen (rule 2).",
            "Therefore, the Chef must be in the Study, leaving the Kitchen for the Butler."
        ],
        "solution_explanation": "Maid is in the Library. Chef cannot be in Library or Kitchen, so Chef is in the Study. This leaves the Kitchen for the Butler.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "logic_003",
        "title": "The Murder Weapon Ownership",
        "category": "logic",
        "difficulty": "easy",
        "description": "Three suspects (Arthur, Beatrice, Charles) each possess one weapon (Dagger, Poison, Pistol).\n1. Arthur does not have the Pistol.\n2. Beatrice has the Poison.",
        "question": "Which weapon does Arthur possess?",
        "acceptable_answer_format": "Type only the weapon name.\n\nExample:\nDagger",
        "accepted_answers": ["Dagger", "dagger", "DAGGER", "The Dagger", "the dagger"],
        "hints": [
            "Beatrice has Poison.",
            "That leaves Dagger and Pistol for Arthur and Charles.",
            "Arthur does NOT have the Pistol, so Arthur must have the Dagger."
        ],
        "solution_explanation": "Beatrice has the Poison. Arthur does not have the Pistol, so Arthur must have the Dagger (leaving the Pistol for Charles).",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "logic_004",
        "title": "The Key Ring Contradiction",
        "category": "logic",
        "difficulty": "easy",
        "description": "Lord Vance says: 'I gave the master key to the Maid.'\nMaid says: 'The Butler took the master key from me.'\nButler says: 'The Maid is lying.'\nDetective note: The Maid is telling the complete truth.",
        "question": "Who currently possesses the master key?",
        "acceptable_answer_format": "Type only the suspect's title or name.\n\nExample:\nButler",
        "accepted_answers": ["Butler", "butler", "BUTLER", "The Butler", "the butler"],
        "hints": [
            "The Maid tells the truth.",
            "The Maid states that the Butler took the key from her.",
            "Therefore, the Butler holds the master key."
        ],
        "solution_explanation": "Since the Maid tells the complete truth, her statement that the Butler took the master key from her confirms the Butler currently possesses it.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "logic_005",
        "title": "The Four Heirs Inheritance",
        "category": "logic",
        "difficulty": "easy",
        "description": "George, Edward, and Henry are three brothers.\n1. George is older than Edward.\n2. Edward is older than Henry.\nRule: The oldest brother inherits the Manor.",
        "question": "Which brother inherits the Manor?",
        "acceptable_answer_format": "Type only the brother's name.\n\nExample:\nGeorge",
        "accepted_answers": ["George", "george", "GEORGE"],
        "hints": [
            "Compare ages: George > Edward.",
            "Edward > Henry.",
            "Order from oldest to youngest: George, Edward, Henry."
        ],
        "solution_explanation": "George is older than Edward, and Edward is older than Henry. George is the oldest brother and inherits the Manor.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "logic_006",
        "title": "Knights and Knaves at the Gala",
        "category": "logic",
        "difficulty": "medium",
        "description": "Lord A says: 'Lord B is a liar.'\nLord B says: 'Lord C is a liar.'\nLord C says: 'Lord A and Lord B are both liars.'\nDetective note: Honest men always tell the truth; liars always lie. Exactly one man is honest.",
        "question": "Which Lord is telling the truth?",
        "acceptable_answer_format": "Type only the Lord's name.\n\nExample:\nLord B",
        "accepted_answers": ["Lord B", "lord b", "LORD B", "B", "b"],
        "hints": [
            "Test Lord A as honest: Then B is a liar -> C is honest (contradicts 'exactly one honest').",
            "Test Lord B as honest: Then C is a liar, and A is a liar (since B is honest, A's claim that B lies is false, so A is a liar!).",
            "Check Lord B = honest: A = liar, B = honest, C = liar. Works perfectly!"
        ],
        "solution_explanation": "If Lord B is honest: C is a liar (matching B's statement), and A is a liar (since A claimed B was a liar, which is false). This satisfies the requirement of exactly one honest man.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "logic_007",
        "title": "The Alibi Verification Grid",
        "category": "logic",
        "difficulty": "medium",
        "description": "The murder occurred at 9:00 PM in the Parlor.\nSuspect 1 was in the Study at 9:00 PM.\nSuspect 2 claims he was in the Parlor at 10:00 PM.\nSuspect 3 was verified in the Billiard Room at 9:00 PM.",
        "question": "Which suspect lacks a verified alibi for the Parlor at 9:00 PM?",
        "acceptable_answer_format": "Type only the suspect number.\n\nExample:\nSuspect 2",
        "accepted_answers": ["Suspect 2", "suspect 2", "SUSPECT 2", "2"],
        "hints": [
            "Murder time: 9:00 PM.",
            "Suspect 1 = Study at 9:00 PM (Alibi OK).",
            "Suspect 3 = Billiard Room at 9:00 PM (Alibi OK). Suspect 2 only accounts for 10:00 PM!"
        ],
        "solution_explanation": "Suspect 1 was in the Study at 9:00 PM and Suspect 3 was in the Billiard Room at 9:00 PM. Suspect 2 only accounted for 10:00 PM, leaving him without an alibi at the 9:00 PM murder time.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "logic_008",
        "title": "The Missing Emerald Ring",
        "category": "logic",
        "difficulty": "medium",
        "description": "Suspect X says: 'Y took the ring.'\nSuspect Y says: 'I did not take the ring.'\nSuspect Z says: 'X is lying.'\nDetective note: Exactly ONE of these statements is TRUE.",
        "question": "Who took the emerald ring?",
        "acceptable_answer_format": "Type only the suspect letter.\n\nExample:\nY",
        "accepted_answers": ["Y", "y", "Suspect Y", "suspect y"],
        "hints": [
            "Notice that X's statement and Y's statement directly contradict each other.",
            "One of X or Y MUST be telling the truth, and the other lying.",
            "Since exactly ONE statement is true, Z's statement must be FALSE! Z says 'X is lying' is False -> X is telling the Truth ('Y took the ring')."
        ],
        "solution_explanation": "X and Y make contradictory claims, so one is telling the truth and the other is lying. Because exactly one statement is true, Z's statement must be false ('X is lying' = false -> X tells the truth). X says Y took the ring, so Y is guilty.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "logic_009",
        "title": "The Poisoned Tea Cup Spectrum",
        "category": "logic",
        "difficulty": "medium",
        "description": "5 tea cups are on the tray: Red, Blue, Green, Yellow, White.\n1. The poison is in a cup of non-primary color (Primary colors: Red, Blue, Yellow).\n2. The poison is NOT in the White cup.",
        "question": "Which colored cup contains the poison?",
        "acceptable_answer_format": "Type only the color name.\n\nExample:\nGreen",
        "accepted_answers": ["Green", "green", "GREEN", "The Green Cup"],
        "hints": [
            "Primary colors are Red, Blue, Yellow.",
            "Non-primary cups on the tray are Green and White.",
            "Rule 2 eliminates White, leaving Green."
        ],
        "solution_explanation": "The non-primary color cups are Green and White. Rule 2 eliminates White, leaving Green as the poisoned cup.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "logic_010",
        "title": "The Dinner Table Seating Arrangement",
        "category": "logic",
        "difficulty": "medium",
        "description": "4 guests were seated around a square table (North, South, East, West).\n1. The Host sat at North.\n2. Suspect A sat directly across from the Host.\n3. Suspect B sat to the Host's Right (West).\n4. Suspect C sat to the Host's Left (East).",
        "question": "Which suspect sat at the East seat?",
        "acceptable_answer_format": "Type only the suspect name.\n\nExample:\nSuspect C",
        "accepted_answers": ["Suspect C", "suspect c", "SUSPECT C", "C", "c"],
        "hints": [
            "Host = North.",
            "Across from Host (South) = Suspect A.",
            "Right of Host (West) = Suspect B. Left of Host (East) = Suspect C."
        ],
        "solution_explanation": "Host = North, Suspect A = South (across from Host), Suspect B = West (Host's Right), Suspect C = East (Host's Left).",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "logic_011",
        "title": "The Five Suspect Alibi Matrix",
        "category": "logic",
        "difficulty": "hard",
        "description": "Four suspects were present at the crime scene:\n1. The killer wore a silk scarf.\n2. The Doctor and Artist wore woolen ties.\n3. The Colonel wore a leather collar.\n4. Baron Raymond wore a silk scarf.",
        "question": "Who is the killer?",
        "acceptable_answer_format": "Type only the suspect's name.\n\nExample:\nBaron Raymond",
        "accepted_answers": ["Baron Raymond", "baron raymond", "BARON RAYMOND", "Baron", "baron"],
        "hints": [
            "Killer's attire: Silk scarf.",
            "Eliminate Doctor (wool), Artist (wool), Colonel (leather).",
            "Baron Raymond is the only suspect who wore a silk scarf."
        ],
        "solution_explanation": "The killer wore a silk scarf. Doctor and Artist wore woolen ties, and the Colonel wore a leather collar. Baron Raymond is the only suspect who wore a silk scarf.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "logic_012",
        "title": "Logical Implications of Guilt",
        "category": "logic",
        "difficulty": "hard",
        "description": "1. If Suspect A is innocent, then Suspect B is guilty.\n2. If Suspect B is guilty, then Suspect C has the weapon.\n3. Forensic evidence proves Suspect C does NOT have the weapon.",
        "question": "Is Suspect A Innocent or Guilty?",
        "acceptable_answer_format": "Type Innocent or Guilty.\n\nExample:\nGuilty",
        "accepted_answers": ["Guilty", "guilty", "GUILTY"],
        "hints": [
            "Work backward from premise 3: C does not have the weapon.",
            "By contrapositive of premise 2: If C doesn't have weapon -> B is NOT guilty.",
            "By contrapositive of premise 1: If B is not guilty -> A is NOT innocent (A is GUILTY)."
        ],
        "solution_explanation": "Since Suspect C does not have the weapon, by contrapositive B is not guilty. If B is not guilty, by contrapositive Suspect A is not innocent. Therefore, Suspect A is GUILTY.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "logic_013",
        "title": "The Counterfeit Note Transaction",
        "category": "logic",
        "difficulty": "hard",
        "description": "Banker says: 'Merchant passed the fake bill.'\nMerchant says: 'Jeweler passed the fake bill.'\nJeweler says: 'Merchant is innocent.'\nDetective note: The person who passed the bill is lying; the innocent suspects tell the truth.",
        "question": "Who passed the counterfeit bill?",
        "acceptable_answer_format": "Type only the suspect's title.\n\nExample:\nMerchant",
        "accepted_answers": ["Merchant", "merchant", "MERCHANT", "The Merchant", "the merchant"],
        "hints": [
            "Notice Merchant and Jeweler contradict each other.",
            "If Merchant passed the bill: Merchant lies ('Jeweler passed it' is False).",
            "Test Merchant: Banker tells truth ('Merchant passed it'), Merchant lies ('Jeweler passed it'), Jeweler lies ('Merchant is innocent')."
        ],
        "solution_explanation": "Banker states Merchant passed the bill (Truth). Merchant claims Jeweler passed it (Liar). Jeweler states Merchant is innocent (Liar). The passer of the bill (Merchant) is the one lying.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "logic_014",
        "title": "The Masquerade Mask Deduction",
        "category": "logic",
        "difficulty": "hard",
        "description": "Three guests wore Red Mask, Blue Mask, Gold Mask.\n1. The killer wore a Gold Mask.\n2. Lady Clara did NOT wear a Gold Mask.\n3. Duke Thomas wore a Red Mask.",
        "question": "Who wore the Gold Mask?",
        "acceptable_answer_format": "Type only the suspect's name.\n\nExample:\nLord Vaughan",
        "accepted_answers": ["Lord Vaughan", "lord vaughan", "LORD VAUGHAN", "Vaughan", "vaughan"],
        "hints": [
            "Three guests: Lady Clara, Duke Thomas, Lord Vaughan.",
            "Duke Thomas = Red Mask.",
            "Lady Clara did NOT wear Gold Mask (so Clara = Blue Mask). Lord Vaughan must wear Gold Mask."
        ],
        "solution_explanation": "Duke Thomas wore the Red Mask. Lady Clara did not wear the Gold Mask, so she wore the Blue Mask. Lord Vaughan must have worn the Gold Mask.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "logic_015",
        "title": "The Four Locks Combination",
        "category": "logic",
        "difficulty": "hard",
        "description": "A 4-digit code (Digits A-B-C-D).\n1. A is double B (A = 2*B).\n2. C is sum of A and B (C = A + B).\n3. D equals 6.\n4. The sum of all four digits is 24.",
        "question": "What is the 4-digit combination?",
        "acceptable_answer_format": "Type only the numerical code.\n\nExample:\n6-3-9-6",
        "accepted_answers": ["6-3-9-6", "6396", "6 3 9 6"],
        "hints": [
            "D = 6. Total sum = 24, so A + B + C = 18.",
            "Substitute C = A + B: A + B + (A + B) = 2(A + B) = 18 -> A + B = 9.",
            "Substitute A = 2B: 2B + B = 3B = 9 -> B = 3, A = 6, C = 9."
        ],
        "solution_explanation": "D=6. Total sum=24, so A+B+C=18. C=A+B implies 2(A+B)=18, so A+B=9. Since A=2B, 3B=9 -> B=3, A=6, C=9. Combination is 6-3-9-6.",
        "time_limit": 450,
        "reward_points": 300
    }
])

# ==============================================================================
# 4. TIMELINE RECONSTRUCTION (15 Puzzles)
# ==============================================================================
all_puzzles.extend([
    {
        "id": "timeline_001",
        "title": "The Manor Security Alarm Sequence",
        "category": "timeline",
        "difficulty": "easy",
        "description": "Reconstruct the chronological sequence of events from log fragments:\nEvents: [A] Security alarm sounded, [B] Victim entered room, [C] Lights went out, [D] Body discovered.",
        "question": "What is the correct event order (e.g. B-C-A-D)?",
        "acceptable_answer_format": "Write the event order using letters separated by hyphens.\n\nExample:\nA-C-B-D",
        "accepted_answers": ["B-C-A-D", "b-c-a-d", "BCAD", "bcad"],
        "hints": [
            "The victim must enter the room before anything happens to him.",
            "The lights were cut before the trap/alarm was tripped.",
            "The body was discovered last after the alarm drew servants."
        ],
        "solution_explanation": "1. Victim entered room (B), 2. Lights went out (C), 3. Security alarm sounded (A), 4. Body discovered (D). Sequence: B-C-A-D.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "timeline_002",
        "title": "The Poisoning Course Timeline",
        "category": "timeline",
        "difficulty": "easy",
        "description": "Dinner service log:\n8:00 PM - Soup served\n8:30 PM - Fish served\n9:00 PM - Roast served\n9:30 PM - Victim collapsed\nMedical fact: The poison used takes exactly 60 minutes to cause collapse.",
        "question": "Which course was poisoned?",
        "acceptable_answer_format": "Type only the meal course name.\n\nExample:\nFish",
        "accepted_answers": ["Fish", "fish", "FISH", "The Fish course", "The fish"],
        "hints": [
            "Collapse time: 9:30 PM.",
            "Poison onset delay: Exactly 60 minutes.",
            "9:30 PM minus 60 minutes = 8:30 PM."
        ],
        "solution_explanation": "Victim collapsed at 9:30 PM. Since the poison takes 60 minutes to act, it was ingested at 8:30 PM, when the Fish course was served.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "timeline_003",
        "title": "The Midnight Express Train Stops",
        "category": "timeline",
        "difficulty": "easy",
        "description": "Train schedule:\n10:00 PM - Departs Station A\n10:30 PM - Arrives Station B\n11:15 PM - Arrives Station C\n12:00 AM - Arrives Station D\nSuspect boarded at Station B and exited at the very next stop.",
        "question": "At which station did the suspect exit?",
        "acceptable_answer_format": "Type only the station name.\n\nExample:\nStation C",
        "accepted_answers": ["Station C", "station c", "STATION C", "C", "c"],
        "hints": [
            "Boarding station: Station B (10:30 PM).",
            "The very next stop on the line is Station C (11:15 PM)."
        ],
        "solution_explanation": "The suspect boarded at Station B (10:30 PM) and exited at the very next stop, which was Station C (11:15 PM).",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "timeline_004",
        "title": "The Doctor's Appointment Log",
        "category": "timeline",
        "difficulty": "easy",
        "description": "Doctor's patient appointment log:\n2:00 PM - Patient Arthur\n2:45 PM - Patient Beatrice\n3:30 PM - Patient Charles\nMurder occurred between 2:50 PM and 3:20 PM.",
        "question": "Which patient was in the doctor's office during the murder?",
        "acceptable_answer_format": "Type only the patient's name.\n\nExample:\nBeatrice",
        "accepted_answers": ["Beatrice", "beatrice", "BEATRICE"],
        "hints": [
            "Murder window: 2:50 PM to 3:20 PM.",
            "Patient Beatrice's appointment started at 2:45 PM and ran until 3:30 PM."
        ],
        "solution_explanation": "The murder occurred between 2:50 PM and 3:20 PM. Patient Beatrice was in the office from 2:45 PM to 3:30 PM.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "timeline_005",
        "title": "The Carriage Arrival Order",
        "category": "timeline",
        "difficulty": "easy",
        "description": "Carriage 2 arrived at 9:00 PM.\nCarriage 1 arrived 10 minutes BEFORE Carriage 2.\nCarriage 3 arrived 15 minutes AFTER Carriage 2.",
        "question": "At what time did Carriage 3 arrive?",
        "acceptable_answer_format": "Type the time.\n\nExample:\n9:15 PM",
        "accepted_answers": ["9:15 PM", "9:15 pm", "9:15PM", "9:15"],
        "hints": [
            "Carriage 2 = 9:00 PM.",
            "Carriage 3 = 9:00 PM + 15 minutes."
        ],
        "solution_explanation": "Carriage 2 arrived at 9:00 PM. Carriage 3 arrived 15 minutes after Carriage 2, making its arrival time 9:15 PM.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "timeline_006",
        "title": "The Lighthouse Signal Disruption",
        "category": "timeline",
        "difficulty": "medium",
        "description": "Lighthouse log:\n10:00 PM - 1 Flash\n10:15 PM - 2 Flashes\n10:30 PM - 3 Flashes\nLog note: Signal disrupted after the 2nd flash sequence but before the 3rd flash sequence.",
        "question": "Between what times did the disruption occur (e.g. 10:15 PM AND 10:30 PM)?",
        "acceptable_answer_format": "Type the time window.\n\nExample:\n10:15 PM AND 10:30 PM",
        "accepted_answers": ["10:15 PM AND 10:30 PM", "10:15 PM and 10:30 PM", "10:15 AND 10:30", "10:15-10:30 PM"],
        "hints": [
            "2nd flash occurred at 10:15 PM.",
            "3rd flash occurred at 10:30 PM."
        ],
        "solution_explanation": "The 2nd flash sequence occurred at 10:15 PM and the 3rd flash sequence was at 10:30 PM. The disruption happened between 10:15 PM and 10:30 PM.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "timeline_007",
        "title": "The Telegram Reading Sequence",
        "category": "timeline",
        "difficulty": "medium",
        "description": "Telegram dispatch timestamps:\nTelegram A sent at 11:00 AM.\nTelegram B sent at 11:20 AM.\nTelegram C sent at 11:45 AM.\nReceiver read Telegram B first, then Telegram A, then Telegram C.",
        "question": "Which telegram was read SECOND?",
        "acceptable_answer_format": "Type only the telegram name.\n\nExample:\nTelegram A",
        "accepted_answers": ["Telegram A", "telegram a", "TELEGRAM A", "A", "a"],
        "hints": [
            "Reading sequence: 1st = Telegram B, 2nd = Telegram A, 3rd = Telegram C."
        ],
        "solution_explanation": "The receiver read Telegram B first, Telegram A second, and Telegram C third. Telegram A was read second.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "timeline_008",
        "title": "The Theater Intermission Murder",
        "category": "timeline",
        "difficulty": "medium",
        "description": "Theater schedule:\nAct I: 8:00 PM - 8:45 PM\nIntermission: 8:45 PM - 9:05 PM\nAct II: 9:05 PM - 9:50 PM\nVictim shot at 9:15 PM during a stage gunshot sound effect.",
        "question": "During which part of the evening did the murder take place?",
        "acceptable_answer_format": "Type only the show section.\n\nExample:\nAct II",
        "accepted_answers": ["Act II", "act ii", "ACT II", "Act 2", "act 2"],
        "hints": [
            "Murder time: 9:15 PM.",
            "Act II runs from 9:05 PM to 9:50 PM."
        ],
        "solution_explanation": "The murder occurred at 9:15 PM, which falls within Act II (9:05 PM to 9:50 PM).",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "timeline_009",
        "title": "The Bank Vault Override Time",
        "category": "timeline",
        "difficulty": "medium",
        "description": "Vault timer was set for 12 hours at 8:00 PM.\nThe override key was used 2 hours earlier than the scheduled opening time.",
        "question": "At what time was the vault opened?",
        "acceptable_answer_format": "Type the time.\n\nExample:\n6:00 AM",
        "accepted_answers": ["6:00 AM", "6:00 am", "6:00AM", "6:00"],
        "hints": [
            "Scheduled opening: 8:00 PM + 12 hours = 8:00 AM.",
            "Opened 2 hours earlier: 8:00 AM minus 2 hours = 6:00 AM."
        ],
        "solution_explanation": "The 12-hour timer set at 8:00 PM scheduled opening for 8:00 AM. Opening 2 hours earlier means the vault opened at 6:00 AM.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "timeline_010",
        "title": "The Servant Duty Schedule",
        "category": "timeline",
        "difficulty": "medium",
        "description": "Servant duty schedule:\nButler: 8:00 PM - 10:00 PM\nFootman: 10:00 PM - 12:00 AM\nGuard: 12:00 AM - 2:00 AM\nMurder occurred at 11:15 PM.",
        "question": "Which servant was on duty at the time of the murder?",
        "acceptable_answer_format": "Type only the servant title.\n\nExample:\nFootman",
        "accepted_answers": ["Footman", "footman", "FOOTMAN", "The Footman", "the footman"],
        "hints": [
            "Murder time: 11:15 PM.",
            "Footman shift covers 10:00 PM to 12:00 AM."
        ],
        "solution_explanation": "The murder occurred at 11:15 PM. The Footman was on duty during the 10:00 PM - 12:00 AM shift.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "timeline_011",
        "title": "The Steamship Timezone Crossing",
        "category": "timeline",
        "difficulty": "hard",
        "description": "Steamship log:\nDeparture: 10:00 PM (Port A time).\nVoyage duration: 4 hours elapsed.\nAt midnight, the ship crossed into a new timezone (+1 hour ahead).",
        "question": "What local time did the ship arrive at Port B?",
        "acceptable_answer_format": "Type the time.\n\nExample:\n3:00 AM",
        "accepted_answers": ["3:00 AM", "3:00 am", "3:00AM", "3:00"],
        "hints": [
            "Departure 10:00 PM + 4 hours elapsed = 2:00 AM (Port A time).",
            "Add +1 hour for the timezone change crossed at midnight.",
            "2:00 AM + 1 hour = 3:00 AM."
        ],
        "solution_explanation": "10:00 PM departure + 4 hours elapsed voyage = 2:00 AM Port A time. Adding +1 hour for the timezone crossing at midnight gives 3:00 AM local arrival time.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "timeline_012",
        "title": "The Carriage Speed Alibi Discrepancy",
        "category": "timeline",
        "difficulty": "hard",
        "description": "Suspect claims he drove a carriage 15 miles in 30 minutes (requires 30 mph average).\nThe maximum possible carriage speed is 15 mph.",
        "question": "Is the suspect's alibi Physically Possible or Impossible?",
        "acceptable_answer_format": "Type Possible or Impossible.\n\nExample:\nImpossible",
        "accepted_answers": ["Impossible", "impossible", "IMPOSSIBLE", "Physically Impossible"],
        "hints": [
            "Distance: 15 miles.",
            "Time: 30 minutes (0.5 hours). Required speed = 15 / 0.5 = 30 mph.",
            "Carriage max speed is 15 mph, so 15 miles takes at least 1 hour."
        ],
        "solution_explanation": "Driving 15 miles in 30 minutes requires an average speed of 30 mph. Since the carriage maximum speed is 15 mph, this alibi is physically IMPOSSIBLE.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "timeline_013",
        "title": "The Clock Tower Chimes Calculation",
        "category": "timeline",
        "difficulty": "hard",
        "description": "The clock tower chimes 4 prelude notes at the top of the hour, followed by deep gongs matching the hour.\nThe detective hears 4 prelude chimes followed by 10 deep gongs.",
        "question": "What time is it?",
        "acceptable_answer_format": "Type the time.\n\nExample:\n10:00",
        "accepted_answers": ["10:00", "10:00 PM", "10:00 AM", "10 o'clock"],
        "hints": [
            "4 prelude chimes signal top of the hour.",
            "Count of deep gongs = Hour of the day (10 gongs = 10 o'clock)."
        ],
        "solution_explanation": "The 4 prelude chimes signal the top of the hour, and the 10 deep gongs indicate 10 o'clock (10:00).",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "timeline_014",
        "title": "The Quadruple Movement Window",
        "category": "timeline",
        "difficulty": "hard",
        "description": "Victim was alone in the study from 9:30 PM to 9:45 PM.\nLord Craven left the parlor at 9:25 PM and returned at 9:50 PM.\nBaron moved 9:00-9:20 PM.\nLady Clara moved 9:50-10:10 PM.",
        "question": "Which suspect was unaccounted for during the victim's 9:30-9:45 PM alone window?",
        "acceptable_answer_format": "Type only the suspect's name.\n\nExample:\nLord Craven",
        "accepted_answers": ["Lord Craven", "lord craven", "LORD CRAVEN", "Craven"],
        "hints": [
            "Victim alone window: 9:30 - 9:45 PM.",
            "Lord Craven's absence: 9:25 PM to 9:50 PM (spans 9:30-9:45 PM completely)."
        ],
        "solution_explanation": "The victim was alone from 9:30 PM to 9:45 PM. Lord Craven left at 9:25 PM and returned at 9:50 PM, making him unaccounted for during that exact window.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "timeline_015",
        "title": "The Thermal Body Decay TOD",
        "category": "timeline",
        "difficulty": "hard",
        "description": "Normal body temperature: 98.6°F.\nCrime scene body temperature measured: 89.6°F.\nBody cooling rate: 1.5°F per hour.",
        "question": "How many hours prior to measurement did the victim die?",
        "acceptable_answer_format": "Type the number of hours.\n\nExample:\n6 hours",
        "accepted_answers": ["6 hours", "6 HOURS", "6", "six hours", "6 Hours"],
        "hints": [
            "Temperature drop = 98.6°F - 89.6°F = 9.0°F.",
            "Divide drop by rate: 9.0 / 1.5 = 6 hours."
        ],
        "solution_explanation": "Body temp drop = 98.6°F - 89.6°F = 9.0°F. At a cooling rate of 1.5°F per hour, 9.0 / 1.5 = 6 hours prior to measurement.",
        "time_limit": 450,
        "reward_points": 300
    }
])

# ==============================================================================
# 5. HIDDEN MESSAGES (15 Puzzles)
# ==============================================================================
all_puzzles.extend([
    {
        "id": "hidden_messages_001",
        "title": "The First Letter Acrostic",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "An anonymous letter contained the following verse:\n**P**lease come at once.\n**O**ver the ridge.\n**I**n the chapel.\n**S**ee the crypt.\n**O**btain key.\n**N**ow hurry.",
        "question": "Extract the secret word formed by the first letter of each line:",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nSECRET",
        "accepted_answers": ["POISON", "poison"],
        "hints": [
            "Look at the first letter of each line.",
            "P-O-I-S-O-N."
        ],
        "solution_explanation": "Extracting the first letter of each line (**P**lease, **O**ver, **I**n, **S**ee, **O**btain, **N**ow) spells POISON.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "hidden_messages_002",
        "title": "Every Second Letter Pattern",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "Extract every second letter from the string: 'X S Y A Z F W E'",
        "question": "What secret word is revealed?",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nSECRET",
        "accepted_answers": ["SAFE", "safe"],
        "hints": [
            "Take letters at position 2, 4, 6, 8.",
            "Position 2 = S, Position 4 = A, Position 6 = F, Position 8 = E."
        ],
        "solution_explanation": "Extracting every second letter from 'X S Y A Z F W E' (positions 2, 4, 6, 8) yields S-A-F-E.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "hidden_messages_003",
        "title": "Every Third Letter Sequence",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "Extract every 3rd letter from string: 'A B D A C G G G E E E R'",
        "question": "What word does it form?",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nSECRET",
        "accepted_answers": ["DAGER", "dager", "DAGGER", "dagger"],
        "hints": [
            "Positions 3, 6, 9, 12.",
            "Pos 3 = D, Pos 6 = A, Pos 9 = E, Pos 12 = R."
        ],
        "solution_explanation": "Extracting every 3rd letter from 'A B D A C G G G E E E R' (positions 3, 6, 9, 12) yields D-A-G-E-R.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "hidden_messages_004",
        "title": "Last Letter Word Cipher",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "Extract the last letter of each word in: 'FROG THOU TAXI MELT YUCK'",
        "question": "What secret word is formed?",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nSECRET",
        "accepted_answers": ["GUILT", "guilt"],
        "hints": [
            "FRO**G** -> G",
            "THO**U** -> U",
            "TAX**I** -> I",
            "MEL**T** -> T"
        ],
        "solution_explanation": "Extracting the last letter of each word in 'FROG THOU TAXI MELT YUCK' (G-U-I-L-T) spells GUILT.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "hidden_messages_005",
        "title": "Capital Letters in Scullery Note",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "Extract only the capital letters from: 'tHe BuTlEr DiD iT'",
        "question": "What capitalized letters emerge?",
        "acceptable_answer_format": "Type only the capitalized letters.\n\nExample:\nHBT LERDDT",
        "accepted_answers": ["HBT LERDDT", "hbt lerddt", "HBTLERDDT"],
        "hints": [
            "Look for uppercase characters.",
            "H, B, T, L, E, R, D, D, T."
        ],
        "solution_explanation": "Extracting only the uppercase characters from 'tHe BuTlEr DiD iT' yields HBT LERDDT.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "hidden_messages_006",
        "title": "Capital Letters Love Letter",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "An intercepted note reads: 'Help Is Desperately Needed In South Hall Entrance Dark.'",
        "question": "Extract the capitalized words forming the secret location:",
        "acceptable_answer_format": "Type only the hidden message.\n\nExample:\nHIDE IN SHED",
        "accepted_answers": ["HIDE IN SHED", "hide in shed"],
        "hints": [
            "Look at the capitalized words in the note.",
            "H-I-D-E I-N S-H-E-D."
        ],
        "solution_explanation": "Reading the capitalized words in the love letter reveals the secret location: HIDE IN SHED.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "hidden_messages_007",
        "title": "Diagonal Word Grid",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "A 4x4 Grid was recovered from a locked cabinet:\nL A B C\nD O E F\nG H O I\nJ K L K",
        "question": "Read top-left to bottom-right main diagonal:",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nSECRET",
        "accepted_answers": ["LOOK", "look"],
        "hints": [
            "Row 1 Col 1 = L.",
            "Row 2 Col 2 = O.",
            "Row 3 Col 3 = O, Row 4 Col 4 = K."
        ],
        "solution_explanation": "Reading from top-left to bottom-right along the main diagonal (Row 1 Col 1=L, Row 2 Col 2=O, Row 3 Col 3=O, Row 4 Col 4=K) spells LOOK.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "hidden_messages_008",
        "title": "Punctuation Exclamation Clue",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "Extract the words immediately following an exclamation mark (!):\n'Hurry! Run quickly! To the! Chapel now!'",
        "question": "What 3 words follow the exclamation marks?",
        "acceptable_answer_format": "Type the extracted phrase.\n\nExample:\nRUN TO CHAPEL",
        "accepted_answers": ["RUN TO CHAPEL", "run to chapel"],
        "hints": [
            "Word after 1st ! = Run.",
            "Word after 2nd ! = To.",
            "Word after 3rd ! = Chapel."
        ],
        "solution_explanation": "Extracting the words immediately following each exclamation mark ('Hurry! Run...', 'quickly! To...', 'the! Chapel...') forms RUN TO CHAPEL.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "hidden_messages_009",
        "title": "Sentence Opening Words",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "Read the FIRST word of each sentence:\n'Meet at dusk. Me near gate. In dark. Study well.'",
        "question": "What 4-word message is formed?",
        "acceptable_answer_format": "Type the extracted phrase.\n\nExample:\nMEET ME IN STUDY",
        "accepted_answers": ["MEET ME IN STUDY", "meet me in study"],
        "hints": [
            "Sentence 1: Meet.",
            "Sentence 2: Me.",
            "Sentence 3: In. Sentence 4: Study."
        ],
        "solution_explanation": "Taking the first word of each sentence ('Meet at dusk. Me near gate. In dark. Study well.') spells MEET ME IN STUDY.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "hidden_messages_010",
        "title": "Reversed Sentence Word Order",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "Reverse the word order in: 'VAULT THE IN IS POISON THE'",
        "question": "Read the reconstructed sentence:",
        "acceptable_answer_format": "Type the decoded sentence.\n\nExample:\nTHE POISON IS IN THE VAULT",
        "accepted_answers": ["THE POISON IS IN THE VAULT", "the poison is in the vault"],
        "hints": [
            "Reverse word sequence from last to first.",
            "THE -> POISON -> IS -> IN -> THE -> VAULT."
        ],
        "solution_explanation": "Reversing the word sequence of 'VAULT THE IN IS POISON THE' from last to first produces 'THE POISON IS IN THE VAULT'.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "hidden_messages_011",
        "title": "Line First-Letter Book Acrostic",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "An acrostic note reads:\n**A**lways watch him.\n**L**ook at hands.\n**I**nspect coat.\n**B**eware trap.\n**I**nspect vault.",
        "question": "What secret word is formed by line initial letters?",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nALIBI",
        "accepted_answers": ["ALIBI", "alibi"],
        "hints": [
            "A-L-I-B-I."
        ],
        "solution_explanation": "Taking the initial letter of each line (**A**lways, **L**ook, **I**nspect, **B**eware, **I**nspect) spells ALIBI.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "hidden_messages_012",
        "title": "Steganographic Number Index Code",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "A secret index code reads: 'Word 3 of: [The red poison vault]'",
        "question": "Extract Word 3:",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nPOISON",
        "accepted_answers": ["POISON", "poison"],
        "hints": [
            "Word 1 = The, Word 2 = red, Word 3 = poison."
        ],
        "solution_explanation": "Selecting Word 3 from '[The red poison vault]' yields POISON.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "hidden_messages_013",
        "title": "Every Fourth Letter Spiral",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "Extract every 4th letter from 'X X X C X X X L X X X U X X X E'",
        "question": "What word is formed?",
        "acceptable_answer_format": "Type only the hidden word.\n\nExample:\nCLUE",
        "accepted_answers": ["CLUE", "clue"],
        "hints": [
            "Pos 4 = C, Pos 8 = L, Pos 12 = U, Pos 16 = E."
        ],
        "solution_explanation": "Extracting every 4th letter from 'X X X C X X X L X X X U X X X E' (positions 4, 8, 12, 16) spells CLUE.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "hidden_messages_014",
        "title": "Palindrome Word Extraction",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "From the list of words [CAT, DEED, DOOR, WALL], select the palindrome.",
        "question": "Which word reads the same forward and backward?",
        "acceptable_answer_format": "Type only the palindrome word.\n\nExample:\nDEED",
        "accepted_answers": ["DEED", "deed"],
        "hints": [
            "D-E-E-D reversed is D-E-E-D."
        ],
        "solution_explanation": "DEED reads identically forward and backward, making it the only palindrome.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "hidden_messages_015",
        "title": "Double Head-Tail Acrostic",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "Combine the first letter of Line 1 (**T**ake note) and the last letter of Line 2 (Go t**o**).",
        "question": "Decode 2-letter destination: Line 1 start **T**, Line 2 end **O**.",
        "acceptable_answer_format": "Type only the 2-letter destination.\n\nExample:\nTO",
        "accepted_answers": ["TO", "to"],
        "hints": [
            "Line 1 start = T.",
            "Line 2 end = O."
        ],
        "solution_explanation": "Combining Line 1 first letter (**T**) and Line 2 last letter (**O**) forms TO.",
        "time_limit": 450,
        "reward_points": 300
    }
])

# ==============================================================================
# 6. CODE BREAKING (15 Puzzles)
# ==============================================================================
all_puzzles.extend([
    {
        "id": "code_breaking_001",
        "title": "The Four-Digit Safe Code Sum",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "The safe code is 4 digits long. The digits sum to 10.\nThe first three digits are 4-3-2.",
        "question": "What is the complete 4-digit code?",
        "acceptable_answer_format": "Type only the numerical code.\n\nExample:\n4321",
        "accepted_answers": ["4321", "4-3-2-1"],
        "hints": [
            "4 + 3 + 2 = 9.",
            "Total sum must equal 10.",
            "10 - 9 = 1. The 4th digit is 1."
        ],
        "solution_explanation": "The sum of the digits must equal 10. 4 + 3 + 2 = 9. 10 - 9 = 1, so the 4th digit is 1. Full code: 4321.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "code_breaking_002",
        "title": "The Letter-to-Number Locker Code",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "Using mapping A=1, B=2, C=3... decode the number sequence '3-1-2'.",
        "question": "What 3-letter word does 3-1-2 represent?",
        "acceptable_answer_format": "Type the decoded word.\n\nExample:\nCAB",
        "accepted_answers": ["CAB", "cab"],
        "hints": [
            "3 = C, 1 = A, 2 = B."
        ],
        "solution_explanation": "Mapping numbers A=1, B=2, C=3: 3=C, 1=A, 2=B spells CAB.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "code_breaking_003",
        "title": "The Fibonacci Lock Sequence",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "The safe dial follows a Fibonacci sequence: 1, 1, 2, 3, 5, 8, ?",
        "question": "What is the next number in the sequence?",
        "acceptable_answer_format": "Type only the number.\n\nExample:\n13",
        "accepted_answers": ["13"],
        "hints": [
            "Each number is the sum of the previous two numbers.",
            "5 + 8 = 13."
        ],
        "solution_explanation": "In the Fibonacci sequence, each number is the sum of the preceding two (5 + 8 = 13).",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "code_breaking_004",
        "title": "The Prime Number Dial",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "A safe lock requires entering consecutive prime numbers: 2, 3, 5, 7, 11, ?",
        "question": "What is the next prime number?",
        "acceptable_answer_format": "Type only the number.\n\nExample:\n13",
        "accepted_answers": ["13"],
        "hints": [
            "List prime numbers greater than 11.",
            "13 is divisible only by 1 and itself."
        ],
        "solution_explanation": "The sequence contains consecutive prime numbers (2, 3, 5, 7, 11). The next prime number is 13.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "code_breaking_005",
        "title": "The Keypad Pattern Code",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "A 4-digit PIN where each digit increases by 2: 1, 3, 5, ?",
        "question": "What is the 4th digit?",
        "acceptable_answer_format": "Type only the digit.\n\nExample:\n7",
        "accepted_answers": ["7"],
        "hints": [
            "Add +2 to each step.",
            "5 + 2 = 7."
        ],
        "solution_explanation": "Each digit increases by +2 (1, 3, 5). 5 + 2 = 7.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "code_breaking_006",
        "title": "The Master Vault Odd Numbers",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "A 4-digit code consists of all consecutive odd numbers starting at 1.",
        "question": "What is the 4-digit code?",
        "acceptable_answer_format": "Type only the numerical code.\n\nExample:\n1357",
        "accepted_answers": ["1357", "1-3-5-7"],
        "hints": [
            "Consecutive odd numbers starting at 1: 1, 3, 5, 7."
        ],
        "solution_explanation": "The consecutive odd numbers starting at 1 are 1, 3, 5, and 7. Code: 1357.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "code_breaking_007",
        "title": "The Clockwise Dial Combination",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "Turn right to 40, turn left 20 steps to 20, turn right 30 steps to 50.",
        "question": "Enter the 3 combination numbers (e.g. 40-20-50):",
        "acceptable_answer_format": "Type the combination separated by hyphens.\n\nExample:\n40-20-50",
        "accepted_answers": ["40-20-50", "40 20 50", "402050"],
        "hints": [
            "List the three stops: 40, 20, 50."
        ],
        "solution_explanation": "The dial turns right to 40, left to 20, and right to 50. Combination: 40-20-50.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "code_breaking_008",
        "title": "The Phone Keypad Word Code",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "Standard telephone keypad (2=ABC, 8=TUV, 4=GHI).\nDecode '2-4-8' using the first letter of each key.",
        "question": "Decode letter sequence from digits 2-4-8 (first letter of each key: A-G-T):",
        "acceptable_answer_format": "Type the decoded letter sequence.\n\nExample:\nAGT",
        "accepted_answers": ["AGT", "agt"],
        "hints": [
            "Key 2 = A, Key 4 = G, Key 8 = T."
        ],
        "solution_explanation": "Key 2=A, Key 4=G, Key 8=T. First letters of keys 2-4-8 spell AGT.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "code_breaking_009",
        "title": "The Binary Telegraph Code",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "Binary mapping: 0001 = 1, 0010 = 2, 0011 = 3, 0100 = ?",
        "question": "What decimal number does binary 0100 represent?",
        "acceptable_answer_format": "Type only the decimal number.\n\nExample:\n4",
        "accepted_answers": ["4"],
        "hints": [
            "Binary 0100 = 2^2 = 4."
        ],
        "solution_explanation": "Binary 0100 equals decimal 4 (0*8 + 1*4 + 0*2 + 0*1 = 4).",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "code_breaking_010",
        "title": "The Arithmetic Sequence Lock",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "Sequence: 4, 9, 14, 19, ?",
        "question": "What is the next number?",
        "acceptable_answer_format": "Type only the number.\n\nExample:\n24",
        "accepted_answers": ["24"],
        "hints": [
            "Add +5 to each term.",
            "19 + 5 = 24."
        ],
        "solution_explanation": "The sequence increases by a common difference of +5 (4, 9, 14, 19). 19 + 5 = 24.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "code_breaking_011",
        "title": "Mastermind Style Code Elimination",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "Code is 4 digits.\n1-2-3-4 has 0 correct digits.\n5-6-7-8 has all 4 correct digits in exact order.",
        "question": "What is the code?",
        "acceptable_answer_format": "Type only the numerical code.\n\nExample:\n5678",
        "accepted_answers": ["5678", "5-6-7-8"],
        "hints": [
            "1-2-3-4 eliminated completely.",
            "5-6-7-8 contains all correct digits."
        ],
        "solution_explanation": "1-2-3-4 has zero correct digits, and 5-6-7-8 contains all 4 correct digits in exact order. The code is 5678.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "code_breaking_012",
        "title": "The Matrix System Key",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "Equations:\nx + 2 = 6 (so x = 4)\ny - x = 1 (so y = 5)\nz = x + y (so z = 9)",
        "question": "Enter key as x-y-z:",
        "acceptable_answer_format": "Type the key separated by hyphens.\n\nExample:\n4-5-9",
        "accepted_answers": ["4-5-9", "459", "4 5 9"],
        "hints": [
            "x = 6 - 2 = 4.",
            "y = 1 + 4 = 5.",
            "z = 4 + 5 = 9."
        ],
        "solution_explanation": "x + 2 = 6 -> x = 4. y - 4 = 1 -> y = 5. z = 4 + 5 = 9. Key: 4-5-9.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "code_breaking_013",
        "title": "Modular Arithmetic Padlock",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "Calculate (17 mod 5):",
        "question": "What is 17 modulo 5 (remainder of 17 / 5)?",
        "acceptable_answer_format": "Type only the remainder number.\n\nExample:\n2",
        "accepted_answers": ["2"],
        "hints": [
            "17 divided by 5 is 3 with remainder 2."
        ],
        "solution_explanation": "17 divided by 5 equals 3 with a remainder of 2. 17 mod 5 = 2.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "code_breaking_014",
        "title": "Multi-Layer Symmetric PIN",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "A 4-digit code is symmetrical (palindrome). First digit is 3. Second digit is 9.",
        "question": "What is the complete 4-digit code?",
        "acceptable_answer_format": "Type only the 4-digit code.\n\nExample:\n3993",
        "accepted_answers": ["3993", "3-9-9-3"],
        "hints": [
            "Symmetrical means digit 4 = digit 1 (3), digit 3 = digit 2 (9)."
        ],
        "solution_explanation": "A symmetrical 4-digit code starting with 3 and 9 mirrors its digits as 3-9-9-3.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "code_breaking_015",
        "title": "The Double Shift Micro-Lock",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "Shift letter 'A' forward by 2 positions, then forward by 3 positions.",
        "question": "What final letter is reached?",
        "acceptable_answer_format": "Type only the final letter.\n\nExample:\nF",
        "accepted_answers": ["F", "f"],
        "hints": [
            "A + 2 = C.",
            "C + 3 = F."
        ],
        "solution_explanation": "Shifting 'A' forward by 2 positions gives 'C'. Shifting 'C' forward by 3 positions gives 'F'.",
        "time_limit": 450,
        "reward_points": 300
    }
])

# ==============================================================================
# 7. WITNESS STATEMENTS (15 Puzzles)
# ==============================================================================
all_puzzles.extend([
    {
        "id": "witness_statements_001",
        "title": "The Rainy Night Alibi Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "Witness depositions:\nWitness A: 'It poured rain heavily all night from 8 PM to 4 AM.'\nWitness B: 'I sat in the garden at 10 PM admiring the bright full moon in a completely clear sky.'\nWeather Log: Heavy downpour & storm all night.",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness B",
        "accepted_answers": ["Witness B", "witness b", "WITNESS B", "B", "b"],
        "hints": [
            "Compare Witness B's clear sky claim with the official Weather Log.",
            "Heavy rain all night makes seeing the moon in a clear sky impossible.",
            "Witness B lied about sitting outside under a clear sky."
        ],
        "solution_explanation": "Weather log confirms heavy rain all night from 8 PM to 4 AM. Witness B's claim of sitting outside admiring a clear full moon at 10 PM is a lie.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "witness_statements_002",
        "title": "The Clock Chimes Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "Witness C: 'I heard the parlor grandfather clock chime 12 full times at 12:30 AM.'\nClockmaker Inspection: The parlor clock chimes once at half-past, and hour counts only at the top of the hour.",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness C",
        "accepted_answers": ["Witness C", "witness c", "WITNESS C", "C", "c"],
        "hints": [
            "Grandfather clocks chime once on half-hours.",
            "Witness C claims 12 chimes at 12:30 AM."
        ],
        "solution_explanation": "Grandfather clocks chime only once on half-hours. Witness C lied about hearing 12 full chimes at 12:30 AM.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "witness_statements_003",
        "title": "The Wall Reflection Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "Witness A: 'I stood in the hallway and saw the killer's face reflected in the brick wall mirror.'\nArchitecture Report: The hallway brick wall contains zero mirrors.",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness A",
        "accepted_answers": ["Witness A", "witness a", "WITNESS A", "A", "a"],
        "hints": [
            "There are no mirrors on the hallway brick wall."
        ],
        "solution_explanation": "The architecture report confirms the hallway brick wall contains zero mirrors. Witness A lied about seeing a reflection.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "witness_statements_004",
        "title": "The Cold Tea Cup Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "Witness B: 'The victim poured steaming hot tea 1 minute before he died at 9:00 PM.'\nForensic Test: The tea cup on the desk was frozen solid with ice.",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness B",
        "accepted_answers": ["Witness B", "witness b", "WITNESS B", "B", "b"],
        "hints": [
            "Steaming tea cannot freeze solid in 1 minute."
        ],
        "solution_explanation": "Steaming hot tea cannot turn into solid ice within 1 minute. Witness B's claim contradicts physical facts.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "witness_statements_005",
        "title": "The Shadow Direction Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "Witness C: 'At high noon (12:00 PM) under the direct overhead sun, the killer's shadow stretched 50 feet due East.'",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness C",
        "accepted_answers": ["Witness C", "witness c", "WITNESS C", "C", "c"],
        "hints": [
            "Direct overhead noon sun casts minimal shadow directly below, not 50 ft East."
        ],
        "solution_explanation": "Under the direct overhead sun at high noon (12:00 PM), a 50-foot shadow stretching East is physically impossible. Witness C lied.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "witness_statements_006",
        "title": "The Footstep Distance Contradiction",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "Witness A: 'I heard the killer take 100 heavy paces walking down the 10-foot scullery hallway.'",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness A",
        "accepted_answers": ["Witness A", "witness a", "WITNESS A", "A", "a"],
        "hints": [
            "100 paces in a 10-foot hallway means each step is 1.2 inches long."
        ],
        "solution_explanation": "Taking 100 paces in a 10-foot hallway would require tiny 1.2-inch steps. Witness A's claim is absurd and false.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "witness_statements_007",
        "title": "The Cold Motor Engine",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "Witness B: 'I just drove my motor car 50 miles at high speed, arriving at 9:00 PM.'\nDetective Inspection at 9:02 PM: The motor car engine block is freezing cold.",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness B",
        "accepted_answers": ["Witness B", "witness b", "WITNESS B", "B", "b"],
        "hints": [
            "Driving 50 miles leaves the engine block hot, not freezing cold."
        ],
        "solution_explanation": "Driving a car 50 miles at high speed leaves the engine block hot. Witness B's freezing cold engine proves he lied.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "witness_statements_008",
        "title": "The Smoke Residue Contradiction",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "Witness C: 'The victim smoked 3 cigars with me right before he died.'\nAutopsy Report: Zero tobacco smoke residue or carbon monoxide in victim's lungs.",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness C",
        "accepted_answers": ["Witness C", "witness c", "WITNESS C", "C", "c"],
        "hints": [
            "Autopsy proves victim inhaled no smoke."
        ],
        "solution_explanation": "Autopsy confirmed zero tobacco smoke residue or carbon monoxide in victim's lungs, disproving Witness C's claim that they smoked 3 cigars.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "witness_statements_009",
        "title": "The Telegram Timestamp Contradiction",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "Witness A: 'I received the victim's telegram at 2:00 PM.'\nTelegraph Office Record: Telegram was dispatched at 4:00 PM.",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness A",
        "accepted_answers": ["Witness A", "witness a", "WITNESS A", "A", "a"],
        "hints": [
            "You cannot receive a telegram before it is sent."
        ],
        "solution_explanation": "Witness A claimed to receive the telegram at 2:00 PM, but the telegraph office records show it was dispatched at 4:00 PM. A message cannot be received before it is sent.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "witness_statements_010",
        "title": "The Spectacles Vision Contradiction",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "Witness B (legally blind without thick glasses): 'I lost my glasses at noon, but at 10 PM in pitch darkness I clearly recognized the killer's facial mole from 100 yards away.'",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness B",
        "accepted_answers": ["Witness B", "witness b", "WITNESS B", "B", "b"],
        "hints": [
            "Blind without glasses + pitch darkness + 100 yards away."
        ],
        "solution_explanation": "Recognizing a facial mole from 100 yards in pitch darkness while legally blind without glasses is physically impossible. Witness B lied.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "witness_statements_011",
        "title": "The Sound Speed Delay Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "Witness C: 'I saw the gunshot flash on the hill 2 miles away and heard the bang at the exact same millisecond.'",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness C",
        "accepted_answers": ["Witness C", "witness c", "WITNESS C", "C", "c"],
        "hints": [
            "Sound travels ~1 mile per 5 seconds. 2 miles takes ~10 seconds."
        ],
        "solution_explanation": "Sound travels approximately 1 mile per 5 seconds. Sound from 2 miles away takes roughly 10 seconds to arrive, not the exact same millisecond. Witness C lied.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "witness_statements_012",
        "title": "The Low Tide Landing Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "Witness A: 'I docked my deep-draft schooner at the high-water pier at 3:00 PM.'\nHarbor Tide Table: 3:00 PM was the lowest ebb tide of the year (pier was completely dry mud).",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness A",
        "accepted_answers": ["Witness A", "witness a", "WITNESS A", "A", "a"],
        "hints": [
            "Deep draft ships cannot dock at dry mud low tide."
        ],
        "solution_explanation": "A deep-draft schooner cannot dock at a pier surrounded by dry mud during the lowest ebb tide of the year. Witness A lied.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "witness_statements_013",
        "title": "The Courtyard Echo Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "Witness B: 'The gun fired from the open West field, but the sound echoed off the West open field.'\nAcoustics Report: Open fields produce zero echoes; echoes require solid walls.",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness B",
        "accepted_answers": ["Witness B", "witness b", "WITNESS B", "B", "b"],
        "hints": [
            "Echoes require a reflecting surface."
        ],
        "solution_explanation": "Open fields have no solid surfaces to reflect sound. Witness B lied about hearing an echo off an open field.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "witness_statements_014",
        "title": "The Sodium Gaslamp Color Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "Witness C: 'Under the monochromatic yellow sodium gaslamp, I clearly distinguished the killer's bright red ribbon from a green ribbon.'",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness C",
        "accepted_answers": ["Witness C", "witness c", "WITNESS C", "C", "c"],
        "hints": [
            "Monochromatic sodium light renders red and green as identical dark gray."
        ],
        "solution_explanation": "Monochromatic yellow sodium light renders red and green as identical shades of dark gray, making color discrimination impossible. Witness C lied.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "witness_statements_015",
        "title": "The Mirror Reading Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "Witness A: 'I read the regular non-reversed handwriting on the note reflected in the mirror across the room.'",
        "question": "Which witness is lying?",
        "acceptable_answer_format": "Type only the witness name.\n\nExample:\nWitness A",
        "accepted_answers": ["Witness A", "witness a", "WITNESS A", "A", "a"],
        "hints": [
            "Handwriting reflected in a mirror appears reversed (mirror writing)."
        ],
        "solution_explanation": "Handwriting reflected in a mirror appears reversed (mirror writing). Witness A lied about reading non-reversed text in a mirror.",
        "time_limit": 450,
        "reward_points": 300
    }
])

# ==============================================================================
# 8. EVIDENCE ANALYSIS (15 Puzzles)
# ==============================================================================
all_puzzles.extend([
    {
        "id": "evidence_analysis_001",
        "title": "Blood Type Matching Analysis",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "Blood sample from weapon: Type AB negative.\nSuspect 1: Type O positive\nSuspect 2: Type A positive\nSuspect 3: Type AB negative",
        "question": "Which suspect matches the blood sample?",
        "acceptable_answer_format": "Type only the suspect number.\n\nExample:\nSuspect 3",
        "accepted_answers": ["Suspect 3", "suspect 3", "SUSPECT 3", "3"],
        "hints": [
            "Compare blood type AB negative to suspects.",
            "Suspect 3 is Type AB negative."
        ],
        "solution_explanation": "Blood sample from the weapon was Type AB negative. Suspect 3 is the only suspect with Type AB negative blood.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "evidence_analysis_002",
        "title": "Shoe Size Footprint Analysis",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "Crime scene mud footprint: Size 11.\nSuspect A: Size 8\nSuspect B: Size 9\nSuspect C: Size 11",
        "question": "Which suspect matches the crime scene footprint?",
        "acceptable_answer_format": "Type only the suspect letter or number.\n\nExample:\nSuspect C",
        "accepted_answers": ["Suspect C", "suspect c", "SUSPECT C", "C", "c"],
        "hints": [
            "Footprint size is 11.",
            "Suspect C wears size 11."
        ],
        "solution_explanation": "Crime scene footprint is Size 11. Suspect C wears Size 11 shoes.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "evidence_analysis_003",
        "title": "Rigor Mortis Time of Death",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "Rigor mortis takes 12 hours to fully set.\nBody discovered at 8:00 AM with full rigor mortis.",
        "question": "At what time the previous evening did death occur?",
        "acceptable_answer_format": "Type the time.\n\nExample:\n8:00 PM",
        "accepted_answers": ["8:00 PM", "8:00 pm", "8:00PM", "8:00"],
        "hints": [
            "8:00 AM minus 12 hours = 8:00 PM."
        ],
        "solution_explanation": "Rigor mortis takes 12 hours to fully set. Discovered at 8:00 AM, death occurred 12 hours prior at 8:00 PM.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "evidence_analysis_004",
        "title": "Fingerprint Pattern Matching",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "Weapon print: Whorl pattern.\nSuspect 1: Arch\nSuspect 2: Loop\nSuspect 3: Whorl",
        "question": "Which suspect matches the print?",
        "acceptable_answer_format": "Type only the suspect number.\n\nExample:\nSuspect 3",
        "accepted_answers": ["Suspect 3", "suspect 3", "SUSPECT 3", "3"],
        "hints": [
            "Whorl pattern matches Suspect 3."
        ],
        "solution_explanation": "Weapon print has a Whorl pattern. Suspect 3 matches the Whorl pattern.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "evidence_analysis_005",
        "title": "Ink Chromatography Analysis",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "Ransom note ink: Water-soluble black ink.\nSuspect A pen: Iron gall ink\nSuspect B pen: Water-soluble black ink\nSuspect C pen: Blue ballpoint",
        "question": "Which suspect's pen was used?",
        "acceptable_answer_format": "Type only the suspect letter or number.\n\nExample:\nSuspect B",
        "accepted_answers": ["Suspect B", "suspect b", "SUSPECT B", "B", "b"],
        "hints": [
            "Water-soluble black ink matches Suspect B."
        ],
        "solution_explanation": "Ransom note ink is water-soluble black ink. Suspect B's pen uses water-soluble black ink.",
        "time_limit": 180,
        "reward_points": 100
    },
    {
        "id": "evidence_analysis_006",
        "title": "Gunpowder Residue Location",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "Residue found on right hand only.\nSuspect A: Left-handed, residue on left hand\nSuspect B: Right-handed, residue on right hand\nSuspect C: No residue",
        "question": "Which suspect fired the weapon?",
        "acceptable_answer_format": "Type only the suspect letter or number.\n\nExample:\nSuspect B",
        "accepted_answers": ["Suspect B", "suspect b", "SUSPECT B", "B", "b"],
        "hints": [
            "Right hand residue matches Suspect B."
        ],
        "solution_explanation": "Gunpowder residue was found on the right hand. Suspect B is right-handed with residue on his right hand.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "evidence_analysis_007",
        "title": "Soil Analysis from Boots",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "Crime scene soil: Red clay.\nSuspect 1 boots: White chalk\nSuspect 2 boots: Red clay\nSuspect 3 boots: Clean",
        "question": "Which suspect walked through the crime scene?",
        "acceptable_answer_format": "Type only the suspect number.\n\nExample:\nSuspect 2",
        "accepted_answers": ["Suspect 2", "suspect 2", "SUSPECT 2", "2"],
        "hints": [
            "Red clay soil matches Suspect 2."
        ],
        "solution_explanation": "Crime scene soil is red clay. Suspect 2's boots match red clay soil.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "evidence_analysis_008",
        "title": "Arsenic Poison Dosage",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "Fatal arsenic dose: 100mg.\nAutopsy findings: 150mg arsenic in stomach, ingested 2 hours prior during dinner served by Chef.",
        "question": "Who served the fatal poisoned meal?",
        "acceptable_answer_format": "Type only the suspect title.\n\nExample:\nChef",
        "accepted_answers": ["Chef", "chef", "CHEF", "The Chef", "the chef"],
        "hints": [
            "Poison ingested during dinner served by Chef."
        ],
        "solution_explanation": "Autopsy revealed 150mg of arsenic ingested 2 hours prior during dinner served by the Chef.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "evidence_analysis_009",
        "title": "Fabric Fiber Matching",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "Window latch snagged fiber: Green velvet.\nSuspect A: Tweed suit\nSuspect B: Green velvet jacket\nSuspect C: Silk gown",
        "question": "Which suspect's clothing matches the fiber?",
        "acceptable_answer_format": "Type only the suspect letter or number.\n\nExample:\nSuspect B",
        "accepted_answers": ["Suspect B", "suspect b", "SUSPECT B", "B", "b"],
        "hints": [
            "Green velvet jacket matches Suspect B."
        ],
        "solution_explanation": "Window latch snagged a green velvet fiber. Suspect B was wearing a green velvet jacket.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "evidence_analysis_010",
        "title": "Glass Splatter Direction",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "Broken glass fragments were found entirely INSIDE the study room.",
        "question": "Was the window broken from OUTSIDE or INSIDE?",
        "acceptable_answer_format": "Type Outside or Inside.\n\nExample:\nOutside",
        "accepted_answers": ["Outside", "outside", "OUTSIDE", "From outside"],
        "hints": [
            "Impact force pushes glass fragments in the direction of blow (into the room)."
        ],
        "solution_explanation": "Glass fragments found entirely inside the study room indicate the impact force came from OUTSIDE.",
        "time_limit": 300,
        "reward_points": 200
    },
    {
        "id": "evidence_analysis_011",
        "title": "Triple Factor Forensic Elimination",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "Crime scene evidence: Blood A+, Footprint Size 10, Tweed fiber.\nSuspect 1: Blood A+, Size 10, Tweed fiber\nSuspect 2: Blood B+, Size 10, Tweed fiber\nSuspect 3: Blood A+, Size 8, Silk fiber",
        "question": "Which suspect matches ALL three evidence factors?",
        "acceptable_answer_format": "Type only the suspect number.\n\nExample:\nSuspect 1",
        "accepted_answers": ["Suspect 1", "suspect 1", "SUSPECT 1", "1"],
        "hints": [
            "Suspect 1 has A+, Size 10, Tweed."
        ],
        "solution_explanation": "Suspect 1 is the only suspect who matches all three criteria: Blood A+, Footprint Size 10, and Tweed fiber.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "evidence_analysis_012",
        "title": "Tox Peak Reaction Timing",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "Strychnine peak toxicity occurs 1 hour after ingestion.\nVictim died of peak toxicity at 10:00 PM.",
        "question": "At what time was the poison ingested?",
        "acceptable_answer_format": "Type the time.\n\nExample:\n9:00 PM",
        "accepted_answers": ["9:00 PM", "9:00 pm", "9:00PM", "9:00"],
        "hints": [
            "10:00 PM minus 1 hour = 9:00 PM."
        ],
        "solution_explanation": "Peak toxicity occurs 1 hour after ingestion. Death at 10:00 PM means poison was ingested at 9:00 PM.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "evidence_analysis_013",
        "title": "Ballistic Rifling Grooves",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "Bullet recovered: Left-hand twist rifling.\nGun A: Right-hand twist\nGun B: Left-hand twist",
        "question": "Which gun fired the fatal shot?",
        "acceptable_answer_format": "Type only the gun designation.\n\nExample:\nGun B",
        "accepted_answers": ["Gun B", "gun b", "GUN B", "B", "b"],
        "hints": [
            "Left-hand twist matches Gun B."
        ],
        "solution_explanation": "Recovered bullet shows left-hand twist rifling. Gun B has left-hand twist rifling.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "evidence_analysis_014",
        "title": "Dental Bite Mark Spacing",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "Bite mark on apple shows missing left upper canine.\nSuspect X: All teeth intact\nSuspect Y: Missing left upper canine",
        "question": "Which suspect bit the apple?",
        "acceptable_answer_format": "Type only the suspect letter.\n\nExample:\nSuspect Y",
        "accepted_answers": ["Suspect Y", "suspect y", "SUSPECT Y", "Y", "y"],
        "hints": [
            "Suspect Y missing left upper canine."
        ],
        "solution_explanation": "The bite mark shows a missing left upper canine. Suspect Y is missing a left upper canine.",
        "time_limit": 450,
        "reward_points": 300
    },
    {
        "id": "evidence_analysis_015",
        "title": "Comprehensive Lab Summary Match",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "Lab report summary: Fingerprint Loop, Footprint Size 9, Blood O negative.\nSuspect Alpha: Loop, Size 9, O negative\nSuspect Beta: Whorl, Size 11, AB positive",
        "question": "Which suspect matches the lab report summary?",
        "acceptable_answer_format": "Type only the suspect designation.\n\nExample:\nSuspect Alpha",
        "accepted_answers": ["Suspect Alpha", "suspect alpha", "SUSPECT ALPHA", "Alpha", "alpha"],
        "hints": [
            "Suspect Alpha matches Loop, Size 9, O-."
        ],
        "solution_explanation": "Suspect Alpha matches all lab summary criteria: Fingerprint Loop, Footprint Size 9, and Blood O negative.",
        "time_limit": 450,
        "reward_points": 300
    }
])

def main():
    prepare_directories()
    print(f"Total puzzles to generate: {len(all_puzzles)}")
    
    counts = {}
    for p in all_puzzles:
        cat = p["category"]
        counts[cat] = counts.get(cat, 0) + 1
        
        filepath = PUZZLES_DIR / cat / f"{p['id']}.json"
        data = {
            "id": p["id"],
            "title": p["title"],
            "category": p["category"],
            "difficulty": p["difficulty"],
            "description": p["description"],
            "question": p["question"],
            "acceptable_answer_format": p["acceptable_answer_format"],
            "accepted_answers": p["accepted_answers"],
            "hints": p["hints"],
            "solution_explanation": p["solution_explanation"],
            "time_limit": p["time_limit"],
            "reward_points": p["reward_points"]
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    print("\nPuzzles created per category:")
    for cat, count in sorted(counts.items()):
        print(f" - {cat}: {count} puzzles")
    
    print("\nAll 120 puzzle JSON files generated successfully!")

if __name__ == "__main__":
    main()
else:
    main()
