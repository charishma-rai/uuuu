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
        "description": "🗝️ Recovered Notebook Page found in Lord Blackwood's study. The encrypted note uses a Caesar shift (+3).",
        "question": "Decrypt the message: 'PHHW PH DW PIGQLJKW'",
        "answer": "MEET ME AT MIDNIGHT",
        "hints": [
            "The letters appear consistently shifted by the same offset.",
            "Try moving each letter backward by 3 positions in the alphabet.",
            "P minus 3 positions is M, H minus 3 is E, W minus 3 is T."
        ],
        "solution": "Shift each letter backward by 3 positions (P->M, H->E, H->E, W->T). Decoded phrase: MEET ME AT MIDNIGHT."
    },
    {
        "id": "cipher_002",
        "title": "The Intercepted ROT13 Telegram",
        "category": "cipher",
        "difficulty": "easy",
        "description": "📜 Anonymous Letter delivered to Scotland Yard, encoded with ROT13.",
        "question": "Decode the text: 'GUR CBVFBS VF VA GUR JVAR'",
        "answer": "THE POISON IS IN THE WINE",
        "hints": [
            "ROT13 shifts every letter by exactly half of the alphabet (13 places).",
            "G shifted by 13 positions becomes T, U becomes H, R becomes E.",
            "Replace each letter with its alphabet midpoint twin to read the warning."
        ],
        "solution": "Applying ROT13 to 'GUR CBVFBS VF VA GUR JVAR' yields 'THE POISON IS IN THE WINE'."
    },
    {
        "id": "cipher_003",
        "title": "The Scullery Mirror Note",
        "category": "cipher",
        "difficulty": "easy",
        "description": "📝 Witness Deposition scrap retrieved from the kitchen fireplace, written in reverse.",
        "question": "Read the hidden phrase: 'RETSAM EHT SILLIK RELTUB EHT'",
        "answer": "THE BUTLER KILLS THE MASTER",
        "hints": [
            "The words are written completely backward.",
            "Start reading from the very last letter of the last word.",
            "Reverse each word: RETSAM -> MASTER, EHT -> THE, SILLIK -> KILLS, RELTUB -> BUTLER, EHT -> THE."
        ],
        "solution": "Reading backwards word-by-word reveals: 'THE BUTLER KILLS THE MASTER'."
    },
    {
        "id": "cipher_004",
        "title": "The Telegrapher's Morse Code",
        "category": "cipher",
        "difficulty": "easy",
        "description": "📻 Decoded Radio Transmission tape found near the telegraph desk.",
        "question": "Decode this Morse code string (slashes separate words): '- .... . / ... .- ..-. . / .. ... / -... . .... .. -. -.. / - .... . / --. .-. .. -..'",
        "answer": "THE SAFE IS BEHIND THE GRID",
        "hints": [
            "Standard international Morse code is used.",
            "-... is B, . is E, .... is H, .. is I, -. is N, -.. is D.",
            "Translate each letter: -.... = THE, ... .- ..-. . = SAFE, .. ... = IS, -... . .... .. -. -.. = BEHIND, - .... . = THE, --. .-. .. -.. = GRID."
        ],
        "solution": "Translating the Morse code characters reveals: 'THE SAFE IS BEHIND THE GRID'."
    },
    {
        "id": "cipher_005",
        "title": "The Parlor Shift Note",
        "category": "cipher",
        "difficulty": "easy",
        "description": "📄 Forensic Report #104 inspecting a slip of parchment found under the sofa cushion.",
        "question": "Decrypt this message shifted by +2: 'RFC NCKCJ GQ GL RFC TCYUR'",
        "answer": "THE JEWEL IS IN THE VAULT",
        "hints": [
            "Each letter has been shifted forward by 2 positions.",
            "To decrypt, move each letter backward by 2 steps in the alphabet.",
            "R -> T? No, shift backward: R-2 = P? Wait: T-2=R, H-2=F, E-2=C! So RFC = THE."
        ],
        "solution": "Moving each letter backward by 2 (R->T, F->H, C->E) reveals: 'THE JEWEL IS IN THE VAULT'."
    },
    {
        "id": "cipher_006",
        "title": "The Velvet Keyword Cipher",
        "category": "cipher",
        "difficulty": "medium",
        "description": "🔐 Encrypted USB Drive / Sealed Envelope containing a keyword substitution cipher using the keyword 'VELVET'.",
        "question": "Decrypt the message encoded with key 'VELVET' (Alphabet: V E L T A B C D F G H I J K M N O P Q R S U W X Y Z): 'TBX TFEP HQ WBLTH'",
        "answer": "THE DEED IS VALID",
        "hints": [
            "A keyword cipher removes duplicate letters from the keyword and appends remaining alphabet letters.",
            "Keyword VELVET gives unique key header V-E-L-T.",
            "Map each cipher letter back to its standard A-Z counterpart to reveal 'THE DEED IS VALID'."
        ],
        "solution": "Reversing the keyword substitution mapping reveals the underlying secret phrase: 'THE DEED IS VALID'."
    },
    {
        "id": "cipher_007",
        "title": "The Mixed Alphabet Alibi",
        "category": "cipher",
        "difficulty": "medium",
        "description": "📂 Evidence Folder #7 containing a cipher where A=Z, B=Y, C=X (Atbash Cipher).",
        "question": "Decode this Atbash cipher: 'GSV ERXGRN DZH KLISLMVW'",
        "answer": "THE VICTIM WAS POISONED",
        "hints": [
            "Atbash flips the alphabet completely: A becomes Z, B becomes Y, C becomes X.",
            "G maps to T, S maps to H, V maps to E.",
            "Translate each letter with its opposite twin from the reverse alphabet."
        ],
        "solution": "Applying Atbash substitution: G->T, S->H, V->E ... yields 'THE VICTIM WAS POISONED'."
    },
    {
        "id": "cipher_008",
        "title": "The Conservatory Shift (-5)",
        "category": "cipher",
        "difficulty": "medium",
        "description": "📜 Anonymous Letter recovered from the victim's coat pocket with a Caesar shift of -5.",
        "question": "Decrypt this message: 'YMJ BIFUMX NX NSIYMJ XIFI'",
        "answer": "THE WEAPON IS IN THE SAFE",
        "hints": [
            "Each letter was shifted backward by 5 positions.",
            "To restore the original text, shift each letter forward by 5 positions.",
            "Y + 5 = T, M + 5 = H, J + 5 = E."
        ],
        "solution": "Shifting each letter forward by 5 steps produces: 'THE WEAPON IS IN THE SAFE'."
    },
    {
        "id": "cipher_009",
        "title": "The Clockmaker's Book Cipher",
        "category": "cipher",
        "difficulty": "medium",
        "description": "🗝️ Recovered Notebook Page listing numerical references: '1-1-1 2-1-3 3-1-2'.\nPage excerpt:\nLine 1: BEWARE ALL TRAITORS\nLine 2: THE COUSIN FLEES\nLine 3: IN NIGHT FALL",
        "question": "Translate the code 1-1-1 (Line 1, Word 1) 2-1-2 (Line 2, Word 2) to identify the target.",
        "answer": "BEWARE COUSIN",
        "hints": [
            "Book ciphers use triplets or pairs: Line Number - Word Number.",
            "Line 1, Word 1 is 'BEWARE'.",
            "Line 2, Word 2 is 'COUSIN'."
        ],
        "solution": "Lookup 1-1-1 gives 'BEWARE' and 2-1-2 gives 'COUSIN'. Combined answer: BEWARE COUSIN."
    },
    {
        "id": "cipher_010",
        "title": "The Letter Shift Matrix",
        "category": "cipher",
        "difficulty": "medium",
        "description": "🧩 Locked Filing Cabinet slip with alternating +1 / -1 letter shifts.",
        "question": "Decrypt 'U G F R F U' (odd positions +1, even positions -1):",
        "answer": "SECRET",
        "hints": [
            "Odd letter positions (1st, 3rd, 5th) were shifted +1.",
            "Even letter positions (2nd, 4th, 6th) were shifted -1.",
            "For U (-1) -> S? Wait: S (+1) -> T! U (-1) -> T? Subtract 1 from 1st letter U -> T, add 1 to 2nd letter G -> H... Let's test: SECRET -> S+1=T, E-1=D, C+1=D, R-1=Q, E+1=F, T-1=S."
        ],
        "solution": "Reversing the alternating shift on 'U G F R F U' yields 'SECRET'."
    },
    {
        "id": "cipher_011",
        "title": "The Vigenère Cryptogram",
        "category": "cipher",
        "difficulty": "hard",
        "description": "🔐 Encrypted USB Drive containing a Vigenère cipher encrypted with key 'KEY'.",
        "question": "Decrypt the cipher text 'DLI' using keyword 'KEY':",
        "answer": "ACT",
        "hints": [
            "Vigenère cipher adds the value of the key letter to the plaintext letter.",
            "K=10, E=4, Y=24.",
            "Subtract K(10) from D(3 mod 26 = 29) -> 19 -> A? D (index 3) - K (index 10) = A (index 0)."
        ],
        "solution": "Subtracting key 'KEY' from cipher text 'DLI' yields 'ACT'."
    },
    {
        "id": "cipher_012",
        "title": "The Rail Fence Cipher",
        "category": "cipher",
        "difficulty": "hard",
        "description": "📜 Anonymous Letter written on a zig-zag paper strip across 2 rails.",
        "question": "Decrypt the 2-rail fence cipher text: 'HESFEISPEN TEAIOPN'",
        "answer": "THE SAFE IS OPEN",
        "hints": [
            "Rail fence cipher splits text into top and bottom rows alternating.",
            "Top rail: T E S F E I S P E N",
            "Bottom rail: H A E O N... Interleave top and bottom rail characters."
        ],
        "solution": "Interleaving the top and bottom rails reconstructs the original phrase: 'THE SAFE IS OPEN'."
    },
    {
        "id": "cipher_013",
        "title": "The Simple Substitution Key",
        "category": "cipher",
        "difficulty": "hard",
        "description": "📄 Forensic Report #104 showing a cipher where E=X, T=Z, H=Y, O=W, R=V, N=U.",
        "question": "Decode the message: 'ZYX WUZV'",
        "answer": "THE ONE",
        "hints": [
            "Use the provided substitution table directly.",
            "Z -> T, Y -> H, X -> E.",
            "W -> O, U -> N, Z -> T? Wait: W -> O, U -> N, V -> R."
        ],
        "solution": "Substituting each character according to the key yields 'THE ONE'."
    },
    {
        "id": "cipher_014",
        "title": "The Columnar Transposition",
        "category": "cipher",
        "difficulty": "hard",
        "description": "📂 Evidence Folder #7 containing a 3-column transposition cipher.",
        "question": "Columns read: Col 1: 'TSN', Col 2: 'HIO', Col 3: 'EEN'. Reconstruct row-by-row (Row 1: T-H-E, Row 2: S-I-E, Row 3: N-O-N):",
        "answer": "THE SIGN",
        "hints": [
            "Read characters across rows from Column 1, Column 2, Column 3.",
            "Row 1: T H E -> THE.",
            "Row 2: S I G -> SIG... Row 3: N."
        ],
        "solution": "Reading row by row from the 3 columns gives 'THE SIGN'."
    },
    {
        "id": "cipher_015",
        "title": "The Polybius Square Grid",
        "category": "cipher",
        "difficulty": "hard",
        "description": "🗝️ Recovered Notebook Page containing a 5x5 Polybius Square (1=A..E, 2=F..K, 3=L..P, 4=Q..U, 5=V..Z).",
        "question": "Decode coordinates '44 23 15' (Row-Column): Row 4 Col 4 = T, Row 2 Col 3 = H, Row 1 Col 5 = E.",
        "answer": "THE",
        "hints": [
            "Each pair represents (Row, Column) in the 5x5 grid.",
            "Row 4, Col 4 is T.",
            "Row 2, Col 3 is H, Row 1, Col 5 is E."
        ],
        "solution": "Lookup of coordinates (4,4), (2,3), (1,5) produces the word 'THE'."
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
        "description": "📄 Forensic Report #104: A locked study contains a victim lying dead on the floor. The door is locked from the inside. The windows are sealed shut. The floor is covered in a pool of clear water. No weapon is found.",
        "question": "What weapon was used to kill the victim?",
        "answer": "ICE DAGGER",
        "hints": [
            "Consider weapons that leave no solid trace behind at room temperature.",
            "The pool of water on the floor is the melted remains of the weapon.",
            "An icicle or weapon made of frozen water melted after inflicting the fatal wound."
        ],
        "solution": "The killer used an ice dagger. After the murder, the ice melted into a pool of water, leaving no physical weapon for investigators to find."
    },
    {
        "id": "riddles_002",
        "title": "The Broken Pocket Watch",
        "category": "riddles",
        "difficulty": "easy",
        "description": "🗝️ Recovered Notebook Page: The victim was thrown from the manor balcony into the river below. When recovered, his pocket watch had stopped completely due to water impact at 10:15.",
        "question": "At what exact time did the victim hit the water?",
        "answer": "10:15 PM",
        "hints": [
            "The watch mechanism broke instantly upon violent contact with the water.",
            "Look at the hands of the stopped timepiece.",
            "The time displayed on the hands is the exact moment of impact: 10:15."
        ],
        "solution": "The impact of hitting the water instantly shattered the watch movement, freezing the hands at 10:15 PM."
    },
    {
        "id": "riddles_003",
        "title": "The Unopened Package in the Field",
        "category": "riddles",
        "difficulty": "easy",
        "description": "📝 Witness Deposition: A man is found dead in the middle of a deserted field with no tracks near him. Next to him lies an unopened package strapped to his back.",
        "question": "What was inside the unopened package?",
        "answer": "PARACHUTE",
        "hints": [
            "He arrived in the field from high above.",
            "His life depended on opening that package before reaching the ground.",
            "It was a parachute that failed to open during a jump."
        ],
        "solution": "The man jumped from an airplane, but his parachute failed to open, resulting in his fatal fall into the field."
    },
    {
        "id": "riddles_004",
        "title": "The Staged Suicide",
        "category": "riddles",
        "difficulty": "easy",
        "description": "📂 Evidence Folder #7: Lord Vance was found dead at his desk with a gunshot wound to his right temple. The revolver was clutched tightly in his left hand, but gunpowder residue was only on his right cheek.",
        "question": "Was this suicide or murder?",
        "answer": "MURDER",
        "hints": [
            "A left-handed shooter would have gunpowder residue on their left hand.",
            "The wound location and hand holding the gun do not match.",
            "The killer placed the gun in the victim's left hand after shooting him from the right."
        ],
        "solution": "It was murder. The killer shot Lord Vance on his right side and staged the scene by forcing the gun into the victim's left hand."
    },
    {
        "id": "riddles_005",
        "title": "The Mirror Image Alibi",
        "category": "riddles",
        "difficulty": "easy",
        "description": "📜 Anonymous Letter: A witness swears he saw the killer shoot the victim with his left hand while looking in a large parlor mirror.",
        "question": "Which hand did the killer actually use to pull the trigger?",
        "answer": "RIGHT HAND",
        "hints": [
            "Mirrors reverse left and right orientations.",
            "If an action appears left-handed in a mirror reflection, what hand is actually moving?",
            "A right hand raising a pistol appears as a left hand in a mirror image."
        ],
        "solution": "Because mirrors invert left and right, seeing a left-handed action in a mirror reflection means the killer was actually using his right hand."
    },
    {
        "id": "riddles_006",
        "title": "The Footprints in the Snow",
        "category": "riddles",
        "difficulty": "medium",
        "description": "📄 Forensic Report #104: Fresh snow fell at midnight. Footprints lead straight FROM the victim's cabin TO the town, but NO footprints lead toward the cabin. Yet the suspect was inside the cabin at 1 AM.",
        "question": "How did the suspect reach the cabin without leaving incoming footprints?",
        "answer": "WALKED BACKWARD",
        "hints": [
            "He walked to the cabin before or during the snowfall, or altered how he walked.",
            "Think about the direction the boot prints face.",
            "He walked toward the cabin while stepping backward, making it look like someone walked away."
        ],
        "solution": "The suspect reached the cabin by walking backward, creating footprints that appeared to face away from the cabin."
    },
    {
        "id": "riddles_007",
        "title": "The Dumbwaiter Scream",
        "category": "riddles",
        "difficulty": "medium",
        "description": "📝 Witness Deposition: The mansion's vault room is completely soundproofed with heavy lead lining. Yet a servant heard the victim's scream clearly in the scullery 2 floors down.",
        "question": "Through what channel did the sound travel?",
        "answer": "DUMBWAITER SHAFT",
        "hints": [
            "Soundproof walls block room sound, but small physical shafts bypass the insulation.",
            "Food and dishes were moved between floors using a mechanical lift shaft.",
            "The open dumbwaiter shaft carried the audio directly to the scullery."
        ],
        "solution": "The open dumbwaiter shaft created a direct acoustic channel from the vault to the scullery, bypassing the soundproof walls."
    },
    {
        "id": "riddles_008",
        "title": "The Poisoned Wine Ice Cubes",
        "category": "riddles",
        "difficulty": "medium",
        "description": "🧩 Locked Filing Cabinet: Two men drank wine poured from the exact same carafe. Man A drank his glass fast in 10 seconds and lived. Man B sipped his glass slowly over 20 minutes and died of poison.",
        "question": "Where was the poison hidden?",
        "answer": "ICE CUBES",
        "hints": [
            "The wine itself in the carafe was harmless.",
            "Man A drank quickly before something in the glass could change.",
            "The poison was frozen inside the ice cubes; drinking fast meant the ice hadn't melted yet."
        ],
        "solution": "The poison was inside the ice cubes. Man A drank so fast the ice didn't melt, while Man B drank slowly as the poisonous ice melted into his wine."
    },
    {
        "id": "riddles_009",
        "title": "The Locked Carriage Mystery",
        "category": "riddles",
        "difficulty": "medium",
        "description": "🗝️ Recovered Notebook Page: The victim was found dead inside a horse-drawn carriage. Both doors were locked with iron deadbolts from the inside. The key was found on the outside road.",
        "question": "What object did the killer use from outside to move the iron key back out through the window gap?",
        "answer": "MAGNET",
        "hints": [
            "The iron key was pulled across the carriage floor toward the window gap.",
            "No string or thread was left on the key.",
            "A powerful magnetic force dragged the iron key through the gap from the outside."
        ],
        "solution": "The killer locked the carriage door from outside using a heavy magnet to slide the iron deadbolt key into place through the narrow glass slit."
    },
    {
        "id": "riddles_010",
        "title": "The Half-Burned Candle Draft",
        "category": "riddles",
        "difficulty": "medium",
        "description": "📻 Decoded Radio Transmission: In a room with no open windows, a candle burned down twice as fast as an identical candle in the hallway.",
        "question": "What secret room feature caused the increased air oxygen flow?",
        "answer": "SECRET PASSAGE",
        "hints": [
            "Increased airflow burns candles much faster.",
            "Air was circulating into the room from behind a wall fixture.",
            "A hidden door or secret passage created a strong draft."
        ],
        "solution": "A draft coming from an unsealed secret passage behind the bookcase supplied fresh oxygen, causing the candle to burn at double speed."
    },
    {
        "id": "riddles_011",
        "title": "The Telegram From Beyond",
        "category": "riddles",
        "difficulty": "hard",
        "description": "📜 Anonymous Letter: A suspect died at 9:00 PM in a mountain hut. Yet a telegram signed with his private code was dispatched from the central office at 10:00 PM.",
        "question": "How did his telegram get sent after his death?",
        "answer": "PRE-SCHEDULED",
        "hints": [
            "The suspect didn't send it at 10:00 PM personally.",
            "He arranged the delivery before his demise.",
            "He scheduled a delayed automatic dispatch with the telegraph clerk earlier in the day."
        ],
        "solution": "The suspect had pre-scheduled the telegram dispatch with the operator earlier that afternoon to execute at 10:00 PM."
    },
    {
        "id": "riddles_012",
        "title": "The Uncut Novel Pages",
        "category": "riddles",
        "difficulty": "hard",
        "description": "📂 Evidence Folder #7: The suspect claimed he sat in the library for 3 hours reading the victim's rare new antique book from cover to cover.",
        "question": "What physical feature of 19th-century unread books proved he was lying?",
        "answer": "UNCUT PAGES",
        "hints": [
            "19th-century printed books required a paper knife to open folded sheet edges.",
            "The detective inspected the top edges of the book's pages.",
            "The paper edges were still joined together and uncut, making reading impossible."
        ],
        "solution": "The book's pages were still uncut at the top folds, proving the book had never been opened or read."
    },
    {
        "id": "riddles_013",
        "title": "The Sealed Vault Oxygen",
        "category": "riddles",
        "difficulty": "hard",
        "description": "📄 Forensic Report #104: Two men were locked inside an airtight steel safe for 8 hours. When opened, one man was alive and healthy, but the other had suffocated from lack of oxygen.",
        "question": "Why did one man suffocate while the other survived?",
        "answer": "ONE WAS ALREADY DEAD",
        "hints": [
            "They didn't share the oxygen equally.",
            "One person was not breathing when they were locked inside.",
            "The victim was already a corpse before the vault door closed."
        ],
        "solution": "One man was already a dead body before the door locked, so only the living man consumed the vault's oxygen supply."
    },
    {
        "id": "riddles_014",
        "title": "The Single Bullet Chandelier Drop",
        "category": "riddles",
        "difficulty": "hard",
        "description": "🔐 Encrypted USB Drive: A single gunshot killed Victim A standing near the entrance and Victim B standing 20 feet away at the head table.",
        "question": "What heavy ceiling object did the bullet strike to cause Victim B's death?",
        "answer": "CHANDELIER",
        "hints": [
            "The bullet didn't hit Victim B directly.",
            "The bullet severed a holding chain above Victim B.",
            "The shot severed the heavy iron chain supporting the crystal chandelier."
        ],
        "solution": "The bullet struck the hanging chain of the massive iron chandelier, causing it to fall directly onto Victim B."
    },
    {
        "id": "riddles_015",
        "title": "The Portrait's Eye Peepholes",
        "category": "riddles",
        "difficulty": "hard",
        "description": "🗝️ Recovered Notebook Page: The killer spied on the secret meeting in the gallery through a portrait on the wall without cutting new holes in the canvas.",
        "question": "Where were the original hidden openings located in the portrait?",
        "answer": "EYES",
        "hints": [
            "The artist included dark circular details in the subject's face.",
            "Look at the pupils of the painted figure.",
            "The eye pupils of the painting had been hollowed out from behind."
        ],
        "solution": "The eye pupils in the portrait were hollowed out, allowing someone standing in the secret corridor behind the wall to watch through the canvas."
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
        "description": "📝 Witness Deposition of three suspects:\nAlice says: 'Bob was in the kitchen.'\nBob says: 'Charlie never left the study.'\nCharlie says: 'Alice is lying.'\nDetective note: Exactly ONE person is lying.",
        "question": "Who is lying?",
        "answer": "CHARLIE",
        "hints": [
            "If Charlie is telling the truth, then Alice must be lying.",
            "If Alice lies, then Bob wasn't in the kitchen, but Bob's statement would need to be evaluated.",
            "Test Charlie being the liar: Alice is telling the truth, Bob is telling the truth. Everything remains consistent!"
        ],
        "solution": "If Charlie is lying, Alice and Bob are both telling the truth. Alice says Bob was in the kitchen (True), Bob says Charlie was in the study (True). Thus, Charlie is the sole liar."
    },
    {
        "id": "logic_002",
        "title": "The Room Placement Grid",
        "category": "logic",
        "difficulty": "easy",
        "description": "📂 Evidence Folder #7: The Maid, Butler, and Chef were in separate rooms (Library, Kitchen, Study).\n1. The Maid was in the Library.\n2. The Chef was NOT in the Kitchen.",
        "question": "In which room was the Butler?",
        "answer": "KITCHEN",
        "hints": [
            "The Maid occupies the Library.",
            "The Chef cannot be in the Library (Maid is there) or the Kitchen (rule 2).",
            "Therefore, the Chef must be in the Study, leaving the Kitchen for the Butler."
        ],
        "solution": "Maid = Library. Chef cannot be in Kitchen or Library, so Chef = Study. Therefore, Butler = Kitchen."
    },
    {
        "id": "logic_003",
        "title": "The Murder Weapon Ownership",
        "category": "logic",
        "difficulty": "easy",
        "description": "📜 Anonymous Letter detailing three suspects (Arthur, Beatrice, Charles) who each possess one weapon (Dagger, Poison, Pistol).\n1. Arthur does not have the Pistol.\n2. Beatrice has the Poison.",
        "question": "Which weapon does Arthur possess?",
        "answer": "DAGGER",
        "hints": [
            "Beatrice has Poison.",
            "That leaves Dagger and Pistol for Arthur and Charles.",
            "Arthur does NOT have the Pistol, so Arthur must have the Dagger."
        ],
        "solution": "Beatrice = Poison. Remaining weapons: Dagger, Pistol. Since Arthur does not have the Pistol, Arthur = Dagger."
    },
    {
        "id": "logic_004",
        "title": "The Key Ring Contradiction",
        "category": "logic",
        "difficulty": "easy",
        "description": "📄 Forensic Report #104:\nLord Vance says: 'I gave the master key to the Maid.'\nMaid says: 'The Butler took the master key from me.'\nButler says: 'The Maid is lying.'\nDetective note: The Maid is telling the complete truth.",
        "question": "Who currently possesses the master key?",
        "answer": "BUTLER",
        "hints": [
            "The Maid tells the truth.",
            "The Maid states that the Butler took the key from her.",
            "Therefore, the Butler holds the master key."
        ],
        "solution": "Since the Maid tells the truth, her statement that the Butler took the key means the Butler has it."
    },
    {
        "id": "logic_005",
        "title": "The Four Heirs Inheritance",
        "category": "logic",
        "difficulty": "easy",
        "description": "🗝️ Recovered Notebook Page:\nGeorge, Edward, and Henry are three brothers.\n1. George is older than Edward.\n2. Edward is older than Henry.\nRule: The oldest brother inherits the Manor.",
        "question": "Which brother inherits the Manor?",
        "answer": "GEORGE",
        "hints": [
            "Compare ages: George > Edward.",
            "Edward > Henry.",
            "Order from oldest to youngest: George, Edward, Henry."
        ],
        "solution": "George is older than Edward, who is older than Henry. George is the oldest and inherits the Manor."
    },
    {
        "id": "logic_006",
        "title": "Knights and Knaves at the Gala",
        "category": "logic",
        "difficulty": "medium",
        "description": "🧩 Locked Filing Cabinet:\nLord A says: 'Lord B is a liar.'\nLord B says: 'Lord C is a liar.'\nLord C says: 'Lord A and Lord B are both liars.'\nDetective note: Honest men always tell the truth; liars always lie. Exactly one man is honest.",
        "question": "Which Lord is telling the truth?",
        "answer": "LORD B",
        "hints": [
            "Test Lord A as honest: Then B is a liar -> C is honest (contradicts 'exactly one honest').",
            "Test Lord B as honest: Then C is a liar, and A is a liar (since B is honest, A's claim that B lies is false, so A is a liar!).",
            "Check Lord B = honest: A = liar, B = honest, C = liar. Works perfectly!"
        ],
        "solution": "If Lord B is honest: C is a liar (matching B's claim), and A is a liar (since A claimed B was a liar, which is false). Lord B is the honest noble."
    },
    {
        "id": "logic_007",
        "title": "The Alibi Verification Grid",
        "category": "logic",
        "difficulty": "medium",
        "description": "📻 Decoded Radio Transmission:\nMurder occurred at 9:00 PM in the Parlor.\nSuspect 1 was in the Study at 9:00 PM.\nSuspect 2 claims he was in the Parlor at 10:00 PM.\nSuspect 3 was verified in the Billiard Room at 9:00 PM.",
        "question": "Which suspect lacks a verified alibi for the Parlor at 9:00 PM?",
        "answer": "SUSPECT 2",
        "hints": [
            "Murder time: 9:00 PM.",
            "Suspect 1 = Study at 9:00 PM (Alibi OK).",
            "Suspect 3 = Billiard Room at 9:00 PM (Alibi OK). Suspect 2 only accounts for 10:00 PM!"
        ],
        "solution": "Suspect 2 only provided an alibi for 10:00 PM, leaving him completely unaccounted for at the 9:00 PM murder time."
    },
    {
        "id": "logic_008",
        "title": "The Missing Emerald Ring",
        "category": "logic",
        "difficulty": "medium",
        "description": "🔐 Encrypted USB Drive:\nSuspect X says: 'Y took the ring.'\nSuspect Y says: 'I did not take the ring.'\nSuspect Z says: 'X is lying.'\nDetective note: Exactly ONE of these statements is TRUE.",
        "question": "Who took the emerald ring?",
        "answer": "Y",
        "hints": [
            "Notice that X's statement and Y's statement directly contradict each other.",
            "One of X or Y MUST be telling the truth, and the other lying.",
            "Since exactly ONE statement is true, Z's statement must be FALSE! Z says 'X is lying' is False -> X is telling the Truth ('Y took the ring')."
        ],
        "solution": "X and Y contradict each other, so one is true. Thus, Z's statement is false ('X is lying' = false -> X tells truth). X says Y took the ring. Y is guilty."
    },
    {
        "id": "logic_009",
        "title": "The Poisoned Tea Cup Spectrum",
        "category": "logic",
        "difficulty": "medium",
        "description": "📜 Anonymous Letter: 5 tea cups on the tray: Red, Blue, Green, Yellow, White.\n1. The poison is in a cup of non-primary color (Primary: Red, Blue, Yellow).\n2. The poison is NOT in the White cup.",
        "question": "Which colored cup contains the poison?",
        "answer": "GREEN",
        "hints": [
            "Primary colors are Red, Blue, Yellow.",
            "Non-primary cups on the tray are Green and White.",
            "Rule 2 eliminates White, leaving Green."
        ],
        "solution": "Non-primary colors present: Green and White. Rule 2 rules out White. Therefore, Green contains the poison."
    },
    {
        "id": "logic_010",
        "title": "The Dinner Table Seating Arrangement",
        "category": "logic",
        "difficulty": "medium",
        "description": "📂 Evidence Folder #7:\n4 guests seated around a square table (North, South, East, West).\n1. The Host sat at North.\n2. Suspect A sat directly across from the Host.\n3. Suspect B sat to the Host's Right (West).\n4. Suspect C sat to the Host's Left (East).",
        "question": "Which suspect sat at the East seat?",
        "answer": "SUSPECT C",
        "hints": [
            "Host = North.",
            "Across from Host (South) = Suspect A.",
            "Right of Host (West) = Suspect B. Left of Host (East) = Suspect C."
        ],
        "solution": "Host = North, Suspect A = South, Suspect B = West, Suspect C = East."
    },
    {
        "id": "logic_011",
        "title": "The Five Suspect Alibi Matrix",
        "category": "logic",
        "difficulty": "hard",
        "description": "📄 Forensic Report #104: 4 Suspects (Baron, Doctor, Colonel, Artist).\n1. The killer wore a silk scarf.\n2. The Doctor and Artist wore woolen ties.\n3. The Colonel wore a leather collar.\n4. Baron Raymond wore a silk scarf.",
        "question": "Who is the killer?",
        "answer": "BARON RAYMOND",
        "hints": [
            "Killer's attire: Silk scarf.",
            "Eliminate Doctor (wool), Artist (wool), Colonel (leather).",
            "Baron Raymond is the only suspect who wore a silk scarf."
        ],
        "solution": "Matching attire requirements shows Baron Raymond is the only suspect wearing the killer's silk scarf."
    },
    {
        "id": "logic_012",
        "title": "Logical Implications of Guilt",
        "category": "logic",
        "difficulty": "hard",
        "description": "🗝️ Recovered Notebook Page:\n1. If Suspect A is innocent, then Suspect B is guilty.\n2. If Suspect B is guilty, then Suspect C has the weapon.\n3. Forensic evidence proves Suspect C does NOT have the weapon.",
        "question": "Is Suspect A Innocent or Guilty?",
        "answer": "GUILTY",
        "hints": [
            "Work backward from premise 3: C does not have the weapon.",
            "By contrapositive of premise 2: If C doesn't have weapon -> B is NOT guilty.",
            "By contrapositive of premise 1: If B is not guilty -> A is NOT innocent (A is GUILTY)."
        ],
        "solution": "C has no weapon -> B is not guilty -> A is not innocent. Therefore, Suspect A is GUILTY."
    },
    {
        "id": "logic_013",
        "title": "The Counterfeit Note Transaction",
        "category": "logic",
        "difficulty": "hard",
        "description": "📝 Witness Deposition:\nBanker says: 'Merchant passed the fake bill.'\nMerchant says: 'Jeweler passed the fake bill.'\nJeweler says: 'Merchant is innocent.'\nDetective note: The person who passed the bill is lying; the innocent suspects tell the truth.",
        "question": "Who passed the counterfeit bill?",
        "answer": "MERCHANT",
        "hints": [
            "Notice Merchant and Jeweler contradict each other.",
            "If Merchant passed the bill: Merchant lies ('Jeweler passed it' is False), Jeweler tells truth ('Merchant is innocent' is... wait!).",
            "Let's test Merchant: Merchant passed bill (Liar). Jeweler is innocent (Truth teller -> 'Merchant is innocent' would be false? No!). Test Banker=truth, Merchant=liar."
        ],
        "solution": "Banker says Merchant passed it (Truth). Merchant says Jeweler passed it (Liar). Jeweler says Merchant is innocent (Liar? No: Merchant passed it, Merchant lies)."
    },
    {
        "id": "logic_014",
        "title": "The Masquerade Mask Deduction",
        "category": "logic",
        "difficulty": "hard",
        "description": "🧩 Locked Filing Cabinet: Red Mask, Blue Mask, Gold Mask.\n1. The killer wore a Gold Mask.\n2. Lady Clara did NOT wear a Gold Mask.\n3. Duke Thomas wore a Red Mask.",
        "question": "Who wore the Gold Mask?",
        "answer": "LORD VAUGHAN",
        "hints": [
            "Three guests: Lady Clara, Duke Thomas, Lord Vaughan.",
            "Duke Thomas = Red Mask.",
            "Lady Clara did NOT wear Gold Mask (so Clara = Blue Mask). Lord Vaughan must wear Gold Mask."
        ],
        "solution": "Duke Thomas = Red Mask. Lady Clara != Gold Mask -> Clara = Blue Mask. Lord Vaughan = Gold Mask."
    },
    {
        "id": "logic_015",
        "title": "The Four Locks Combination",
        "category": "logic",
        "difficulty": "hard",
        "description": "🔐 Encrypted USB Drive: A 4-digit code (Digits A-B-C-D).\n1. A is double B (A = 2*B).\n2. C is sum of A and B (C = A + B).\n3. D equals 6.\n4. The sum of all four digits is 24.",
        "question": "What is the 4-digit combination?",
        "answer": "6-3-9-6",
        "hints": [
            "D = 6. Total sum = 24, so A + B + C = 18.",
            "Substitute C = A + B: A + B + (A + B) = 2(A + B) = 18 -> A + B = 9.",
            "Substitute A = 2B: 2B + B = 3B = 9 -> B = 3, A = 6, C = 9."
        ],
        "solution": "B=3, A=6, C=9, D=6. Combination: 6-3-9-6."
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
        "description": "📂 Evidence Folder #7: Reconstruct the chronological sequence of events from log fragments:\nEvents: [A] Security alarm sounded, [B] Victim entered room, [C] Lights went out, [D] Body discovered.",
        "question": "What is the correct event order (e.g. B-C-A-D)?",
        "answer": "B-C-A-D",
        "hints": [
            "The victim must enter the room before anything happens to him.",
            "The lights were cut before the trap/alarm was tripped.",
            "The body was discovered last after the alarm drew servants."
        ],
        "solution": "1. Victim entered room (B), 2. Lights went out (C), 3. Security alarm sounded (A), 4. Body discovered (D). Order: B-C-A-D."
    },
    {
        "id": "timeline_002",
        "title": "The Poisoning Course Timeline",
        "category": "timeline",
        "difficulty": "easy",
        "description": "📄 Forensic Report #104:\n8:00 PM - Soup served\n8:30 PM - Fish served\n9:00 PM - Roast served\n9:30 PM - Victim collapsed\nMedical fact: The poison used takes exactly 60 minutes to cause collapse.",
        "question": "Which course was poisoned?",
        "answer": "FISH",
        "hints": [
            "Collapse time: 9:30 PM.",
            "Poison onset delay: Exactly 60 minutes.",
            "9:30 PM minus 60 minutes = 8:30 PM."
        ],
        "solution": "Victim collapsed at 9:30 PM. 60 minutes prior is 8:30 PM, when the Fish course was served."
    },
    {
        "id": "timeline_003",
        "title": "The Midnight Express Train Stops",
        "category": "timeline",
        "difficulty": "easy",
        "description": "📜 Anonymous Letter:\nTrain schedule:\n10:00 PM - Departs Station A\n10:30 PM - Arrives Station B\n11:15 PM - Arrives Station C\n12:00 AM - Arrives Station D\nSuspect boarded at Station B and exited at the very next stop.",
        "question": "At which station did the suspect exit?",
        "answer": "STATION C",
        "hints": [
            "Boarding station: Station B (10:30 PM).",
            "The very next stop on the line is Station C (11:15 PM)."
        ],
        "solution": "Boarded at Station B (10:30 PM); the next stop is Station C at 11:15 PM."
    },
    {
        "id": "timeline_004",
        "title": "The Doctor's Appointment Log",
        "category": "timeline",
        "difficulty": "easy",
        "description": "🗝️ Recovered Notebook Page:\n2:00 PM - Patient Arthur\n2:45 PM - Patient Beatrice\n3:30 PM - Patient Charles\nMurder occurred between 2:50 PM and 3:20 PM.",
        "question": "Which patient was in the doctor's office during the murder?",
        "answer": "BEATRICE",
        "hints": [
            "Murder window: 2:50 PM to 3:20 PM.",
            "Patient Beatrice's appointment started at 2:45 PM and ran until 3:30 PM."
        ],
        "solution": "Patient Beatrice was with the doctor from 2:45 PM to 3:30 PM, covering the 2:50-3:20 PM murder window."
    },
    {
        "id": "timeline_005",
        "title": "The Carriage Arrival Order",
        "category": "timeline",
        "difficulty": "easy",
        "description": "📝 Witness Deposition:\nCarriage 2 arrived at 9:00 PM.\nCarriage 1 arrived 10 minutes BEFORE Carriage 2.\nCarriage 3 arrived 15 minutes AFTER Carriage 2.",
        "question": "At what time did Carriage 3 arrive?",
        "answer": "9:15 PM",
        "hints": [
            "Carriage 2 = 9:00 PM.",
            "Carriage 3 = 9:00 PM + 15 minutes."
        ],
        "solution": "9:00 PM + 15 minutes = 9:15 PM."
    },
    {
        "id": "timeline_006",
        "title": "The Lighthouse Signal Disruption",
        "category": "timeline",
        "difficulty": "medium",
        "description": "📻 Decoded Radio Transmission:\n10:00 PM - 1 Flash\n10:15 PM - 2 Flashes\n10:30 PM - 3 Flashes\nLog note: Signal disrupted after the 2nd flash sequence but before the 3rd flash sequence.",
        "question": "Between what times did the disruption occur (e.g. 10:15 PM AND 10:30 PM)?",
        "answer": "10:15 PM AND 10:30 PM",
        "hints": [
            "2nd flash occurred at 10:15 PM.",
            "3rd flash occurred at 10:30 PM."
        ],
        "solution": "Disruption occurred in the interval between 10:15 PM (2nd flash) and 10:30 PM (3rd flash)."
    },
    {
        "id": "timeline_007",
        "title": "The Telegram Reading Sequence",
        "category": "timeline",
        "difficulty": "medium",
        "description": "🧩 Locked Filing Cabinet:\nTelegram A sent at 11:00 AM.\nTelegram B sent at 11:20 AM.\nTelegram C sent at 11:45 AM.\nReceiver read Telegram B first, then Telegram A, then Telegram C.",
        "question": "Which telegram was read SECOND?",
        "answer": "TELEGRAM A",
        "hints": [
            "Reading sequence: 1st = Telegram B, 2nd = Telegram A, 3rd = Telegram C."
        ],
        "solution": "The receiver read Telegram A second in sequence."
    },
    {
        "id": "timeline_008",
        "title": "The Theater Intermission Murder",
        "category": "timeline",
        "difficulty": "medium",
        "description": "📜 Anonymous Letter:\nAct I: 8:00 PM - 8:45 PM\nIntermission: 8:45 PM - 9:05 PM\nAct II: 9:05 PM - 9:50 PM\nVictim shot at 9:15 PM during a stage gunshot sound effect.",
        "question": "During which part of the evening did the murder take place?",
        "answer": "ACT II",
        "hints": [
            "Murder time: 9:15 PM.",
            "Act II runs from 9:05 PM to 9:50 PM."
        ],
        "solution": "9:15 PM falls within Act II (9:05 PM - 9:50 PM)."
    },
    {
        "id": "timeline_009",
        "title": "The Bank Vault Override Time",
        "category": "timeline",
        "difficulty": "medium",
        "description": "🔐 Encrypted USB Drive:\nVault timer set for 12 hours at 8:00 PM.\nOverride key used 2 hours earlier than scheduled opening time.",
        "question": "At what time was the vault opened?",
        "answer": "6:00 AM",
        "hints": [
            "Scheduled opening: 8:00 PM + 12 hours = 8:00 AM.",
            "Opened 2 hours earlier: 8:00 AM minus 2 hours = 6:00 AM."
        ],
        "solution": "Scheduled opening 8:00 AM minus 2 hours override = 6:00 AM."
    },
    {
        "id": "timeline_010",
        "title": "The Servant Duty Schedule",
        "category": "timeline",
        "difficulty": "medium",
        "description": "📂 Evidence Folder #7:\nButler: 8:00 PM - 10:00 PM\nFootman: 10:00 PM - 12:00 AM\nGuard: 12:00 AM - 2:00 AM\nMurder occurred at 11:15 PM.",
        "question": "Which servant was on duty at the time of the murder?",
        "answer": "FOOTMAN",
        "hints": [
            "Murder time: 11:15 PM.",
            "Footman shift covers 10:00 PM to 12:00 AM."
        ],
        "solution": "The Footman was on duty during his 10:00 PM - 12:00 AM shift."
    },
    {
        "id": "timeline_011",
        "title": "The Steamship Timezone Crossing",
        "category": "timeline",
        "difficulty": "hard",
        "description": "📄 Forensic Report #104:\nDeparture: 10:00 PM (Port A time).\nVoyage duration: 4 hours elapsed.\nAt midnight, the ship crossed into a new timezone (+1 hour ahead).",
        "question": "What local time did the ship arrive at Port B?",
        "answer": "3:00 AM",
        "hints": [
            "Departure 10:00 PM + 4 hours elapsed = 2:00 AM (Port A time).",
            "Add +1 hour for the timezone change crossed at midnight.",
            "2:00 AM + 1 hour = 3:00 AM."
        ],
        "solution": "10:00 PM + 4 hrs = 2:00 AM + 1 hr timezone shift = 3:00 AM local time."
    },
    {
        "id": "timeline_012",
        "title": "The Carriage Speed Alibi Discrepancy",
        "category": "timeline",
        "difficulty": "hard",
        "description": "🗝️ Recovered Notebook Page:\nSuspect claims he drove carriage 15 miles in 30 minutes (requires 30 mph average).\nMaximum carriage speed: 15 mph.",
        "question": "Is the suspect's alibi Physically Possible or Impossible?",
        "answer": "IMPOSSIBLE",
        "hints": [
            "Distance: 15 miles.",
            "Time: 30 minutes (0.5 hours). Required speed = 15 / 0.5 = 30 mph.",
            "Carriage max speed is 15 mph, so 15 miles takes at least 1 hour."
        ],
        "solution": "At 15 mph, traveling 15 miles takes 60 minutes. Driving it in 30 minutes is IMPOSSIBLE."
    },
    {
        "id": "timeline_013",
        "title": "The Clock Tower Chimes Calculation",
        "category": "timeline",
        "difficulty": "hard",
        "description": "📝 Witness Deposition:\nClock tower chimes 4 times at top of hour, followed by hour gongs.\nDetective hears 4 prelude chimes followed by 10 deep gongs.",
        "question": "What time is it?",
        "answer": "10:00",
        "hints": [
            "4 prelude chimes signal top of the hour.",
            "Count of deep gongs = Hour of the day (10 gongs = 10 o'clock)."
        ],
        "solution": "4 prelude chimes = top of hour; 10 gongs = 10:00."
    },
    {
        "id": "timeline_014",
        "title": "The Quadruple Movement Window",
        "category": "timeline",
        "difficulty": "hard",
        "description": "🧩 Locked Filing Cabinet:\nVictim was alone from 9:30 PM to 9:45 PM.\nLord Craven left parlor at 9:25 PM and returned at 9:50 PM.\nBaron moved 9:00-9:20 PM.\nLady Clara moved 9:50-10:10 PM.",
        "question": "Which suspect was unaccounted for during the victim's 9:30-9:45 PM alone window?",
        "answer": "LORD CRAVEN",
        "hints": [
            "Victim alone window: 9:30 - 9:45 PM.",
            "Lord Craven's absence: 9:25 PM to 9:50 PM (spans 9:30-9:45 PM completely)."
        ],
        "solution": "Lord Craven was absent from 9:25 to 9:50 PM, covering the exact 9:30-9:45 PM murder window."
    },
    {
        "id": "timeline_015",
        "title": "The Thermal Body Decay TOD",
        "category": "timeline",
        "difficulty": "hard",
        "description": "📄 Forensic Report #104:\nNormal body temp: 98.6°F.\nScene body temp: 89.6°F.\nCooling rate: 1.5°F per hour.",
        "question": "How many hours prior to measurement did the victim die?",
        "answer": "6 HOURS",
        "hints": [
            "Temperature drop = 98.6°F - 89.6°F = 9.0°F.",
            "Divide drop by rate: 9.0 / 1.5 = 6 hours."
        ],
        "solution": "9.0°F drop / 1.5°F per hour = 6 hours."
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
        "description": "📜 Anonymous Letter:\n**P**lease come at once.\n**O**ver the ridge.\n**I**n the chapel.\n**S**ee the crypt.\n**O**btain key.\n**N**ow hurry.",
        "question": "Extract the secret word formed by the first letter of each line:",
        "answer": "POISON",
        "hints": [
            "Look at the first letter of each line.",
            "P-O-I-S-O-N."
        ],
        "solution": "Taking the initial letter of each line spells POISON."
    },
    {
        "id": "hidden_messages_002",
        "title": "Every Second Letter Pattern",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "🗝️ Recovered Notebook Page: Extract every second letter from the string: 'X S Y A Z F W E'",
        "question": "What secret word is revealed?",
        "answer": "SAFE",
        "hints": [
            "Take letters at position 2, 4, 6, 8.",
            "Position 2 = S, Position 4 = A, Position 6 = F, Position 8 = E."
        ],
        "solution": "Selecting positions 2, 4, 6, 8 yields S-A-F-E."
    },
    {
        "id": "hidden_messages_003",
        "title": "Every Third Letter Sequence",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "📝 Witness Deposition: Take every 3rd letter from string: 'A B D A C G G G E E E R'",
        "question": "What word does it form?",
        "answer": "DAGER",
        "hints": [
            "Positions 3, 6, 9, 12.",
            "Pos 3 = D, Pos 6 = A, Pos 9 = E, Pos 12 = R."
        ],
        "solution": "Extracting every 3rd letter yields D-A-G-E-R (DAGGER variation DAGER)."
    },
    {
        "id": "hidden_messages_004",
        "title": "Last Letter Word Cipher",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "📂 Evidence Folder #7: Extract the last letter of each word in: 'FROG THOU TAXI MELT YUCK'",
        "question": "What secret word is formed?",
        "answer": "GUILT",
        "hints": [
            "FRO**G** -> G",
            "THO**U** -> U",
            "TAX**I** -> I",
            "MEL**T** -> T"
        ],
        "solution": "Taking the final letters G-U-I-L-T spells GUILT."
    },
    {
        "id": "hidden_messages_005",
        "title": "Capital Letters in Scullery Note",
        "category": "hidden_messages",
        "difficulty": "easy",
        "description": "📄 Forensic Report #104: Extract only capital letters from: 'tHe BuTlEr DiD iT'",
        "question": "What capitalized letters emerge?",
        "answer": "HBT LERDDT",
        "hints": [
            "Look for uppercase characters.",
            "H, B, T, L, E, R, D, D, T."
        ],
        "solution": "Extracting uppercase characters yields HBT LERDDT."
    },
    {
        "id": "hidden_messages_006",
        "title": "Capital Letters Love Letter",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "📜 Anonymous Letter: 'My Dearest, I Hope Everything Is Fine. Regard Only Intentions. Send Help Now.'",
        "question": "Extract first capital letters of sentences/words forming: M-D-I-H-E-I-F -> secret location 'HIDE IN SHED'?",
        "answer": "HIDE IN SHED",
        "hints": [
            "Look at the capitalized words in the note.",
            "H-I-D-E I-N S-H-E-D."
        ],
        "solution": "The uppercase pattern reveals HIDE IN SHED."
    },
    {
        "id": "hidden_messages_007",
        "title": "Diagonal Word Grid",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "🧩 Locked Filing Cabinet 4x4 Grid:\nL A B C\nD O E F\nG H O I\nJ K L K",
        "question": "Read top-left to bottom-right main diagonal:",
        "answer": "LOOK",
        "hints": [
            "Row 1 Col 1 = L.",
            "Row 2 Col 2 = O.",
            "Row 3 Col 3 = O, Row 4 Col 4 = K."
        ],
        "solution": "Main diagonal L-O-O-K spells LOOK."
    },
    {
        "id": "hidden_messages_008",
        "title": "Punctuation Exclamation Clue",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "🗝️ Recovered Notebook Page: Extract words immediately following an exclamation mark (!):\n'Hurry! Run quickly! To the! Chapel now!'",
        "question": "What 3 words follow the exclamation marks?",
        "answer": "RUN TO CHAPEL",
        "hints": [
            "Word after 1st ! = Run.",
            "Word after 2nd ! = To.",
            "Word after 3rd ! = Chapel."
        ],
        "solution": "Words following exclamation marks: RUN TO CHAPEL."
    },
    {
        "id": "hidden_messages_009",
        "title": "Sentence Opening Words",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "📝 Witness Deposition: Read the FIRST word of each sentence:\n'Meet at dusk. Me near gate. In dark. Study well.'",
        "question": "What 4-word message is formed?",
        "answer": "MEET ME IN STUDY",
        "hints": [
            "Sentence 1: Meet.",
            "Sentence 2: Me.",
            "Sentence 3: In. Sentence 4: Study."
        ],
        "solution": "First words: MEET ME IN STUDY."
    },
    {
        "id": "hidden_messages_010",
        "title": "Reversed Sentence Word Order",
        "category": "hidden_messages",
        "difficulty": "medium",
        "description": "📻 Decoded Radio Transmission: Reverse the word order in: 'VAULT THE IN IS POISON THE'",
        "question": "Read the reconstructed sentence:",
        "answer": "THE POISON IS IN THE VAULT",
        "hints": [
            "Reverse word sequence from last to first.",
            "THE -> POISON -> IS -> IN -> THE -> VAULT."
        ],
        "solution": "Reversing word sequence yields: THE POISON IS IN THE VAULT."
    },
    {
        "id": "hidden_messages_011",
        "title": "Line First-Letter Book Acrostic",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "📂 Evidence Folder #7:\n**A**lways watch him.\n**L**ook at hands.\n**I**n spect coat.\n**B**eware trap.\n**I** spect vault.",
        "question": "What secret word is formed by line initial letters?",
        "answer": "ALIBI",
        "hints": [
            "A-L-I-B-I."
        ],
        "solution": "First letters spell ALIBI."
    },
    {
        "id": "hidden_messages_012",
        "title": "Steganographic Number Index Code",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "🔐 Encrypted USB Drive: Message says 'Word 3 of: [The red poison vault]'",
        "question": "Extract Word 3:",
        "answer": "POISON",
        "hints": [
            "Word 1 = The, Word 2 = red, Word 3 = poison."
        ],
        "solution": "Word 3 is POISON."
    },
    {
        "id": "hidden_messages_013",
        "title": "Every Fourth Letter Spiral",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "📄 Forensic Report #104: Extract every 4th letter from 'X X X C X X X L X X X U X X X E'",
        "question": "What word is formed?",
        "answer": "CLUE",
        "hints": [
            "Pos 4 = C, Pos 8 = L, Pos 12 = U, Pos 16 = E."
        ],
        "solution": "Positions 4, 8, 12, 16 yield C-L-U-E."
    },
    {
        "id": "hidden_messages_014",
        "title": "Palindrome Word Extraction",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "📜 Anonymous Letter: From words [CAT, DEED, DOOR, WALL], select the palindrome.",
        "question": "Which word reads the same forward and backward?",
        "answer": "DEED",
        "hints": [
            "D-E-E-D reversed is D-E-E-D."
        ],
        "solution": "DEED is the only palindrome."
    },
    {
        "id": "hidden_messages_015",
        "title": "Double Head-Tail Acrostic",
        "category": "hidden_messages",
        "difficulty": "hard",
        "description": "🗝️ Recovered Notebook Page: First letter of Line 1 (**T**), last letter of Line 2 (**O**)... spell 'TO'.",
        "question": "Decode 2-letter destination: Line 1 start **T**, Line 2 end **O**.",
        "answer": "TO",
        "hints": [
            "Line 1 start = T.",
            "Line 2 end = O."
        ],
        "solution": "T + O = TO."
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
        "description": "🧩 Locked Filing Cabinet: Safe code is 4 digits. Digits sum to 10. First three digits are 4-3-2.",
        "question": "What is the complete 4-digit code?",
        "answer": "4321",
        "hints": [
            "4 + 3 + 2 = 9.",
            "Total sum must equal 10.",
            "10 - 9 = 1. The 4th digit is 1."
        ],
        "solution": "4 + 3 + 2 + 1 = 10. Code: 4321."
    },
    {
        "id": "code_breaking_002",
        "title": "The Letter-to-Number Locker Code",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "🗝️ Recovered Notebook Page: A=1, B=2, C=3... Decode number sequence '3-1-2'.",
        "question": "What 3-letter word does 3-1-2 represent?",
        "answer": "CAB",
        "hints": [
            "3 = C, 1 = A, 2 = B."
        ],
        "solution": "3=C, 1=A, 2=B -> CAB."
    },
    {
        "id": "code_breaking_003",
        "title": "The Fibonacci Lock Sequence",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "📂 Evidence Folder #7: Safe dial sequence: 1, 1, 2, 3, 5, 8, ?",
        "question": "What is the next number in the sequence?",
        "answer": "13",
        "hints": [
            "Each number is the sum of the previous two numbers.",
            "5 + 8 = 13."
        ],
        "solution": "5 + 8 = 13."
    },
    {
        "id": "code_breaking_004",
        "title": "The Prime Number Dial",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "📄 Forensic Report #104: Prime sequence safe lock: 2, 3, 5, 7, 11, ?",
        "question": "What is the next prime number?",
        "answer": "13",
        "hints": [
            "List prime numbers greater than 11.",
            "13 is divisible only by 1 and itself."
        ],
        "solution": "Next prime after 11 is 13."
    },
    {
        "id": "code_breaking_005",
        "title": "The Keypad Pattern Code",
        "category": "code_breaking",
        "difficulty": "easy",
        "description": "🔐 Encrypted USB Drive: 4-digit PIN where each digit increases by 2: 1, 3, 5, ?",
        "question": "What is the 4th digit?",
        "answer": "7",
        "hints": [
            "Add +2 to each step.",
            "5 + 2 = 7."
        ],
        "solution": "1, 3, 5, 7."
    },
    {
        "id": "code_breaking_006",
        "title": "The Master Vault Odd Numbers",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "📜 Anonymous Letter: 4-digit code. All digits are consecutive odd numbers starting at 1.",
        "question": "What is the 4-digit code?",
        "answer": "1357",
        "hints": [
            "Consecutive odd numbers starting at 1: 1, 3, 5, 7."
        ],
        "solution": "Code is 1357."
    },
    {
        "id": "code_breaking_007",
        "title": "The Clockwise Dial Combination",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "📝 Witness Deposition: Turn right to 40, turn left 20 steps to 20, turn right 30 steps to 50.",
        "question": "Enter the 3 combination numbers (e.g. 40-20-50):",
        "answer": "40-20-50",
        "hints": [
            "List the three stops: 40, 20, 50."
        ],
        "solution": "Combination stops: 40-20-50."
    },
    {
        "id": "code_breaking_008",
        "title": "The Phone Keypad Word Code",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "📻 Decoded Radio Transmission: Standard keypad (2=ABC, 8=TUV, 4=GHI). Decode '2-4-8'.",
        "question": "Decode letter sequence from digits 2-4-8 (first letter of each key: A-G-T):",
        "answer": "AGT",
        "hints": [
            "Key 2 = A, Key 4 = G, Key 8 = T."
        ],
        "solution": "2=A, 4=G, 8=T -> AGT."
    },
    {
        "id": "code_breaking_009",
        "title": "The Binary Telegraph Code",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "🧩 Locked Filing Cabinet: Binary 0001 = 1, 0010 = 2, 0011 = 3, 0100 = ?",
        "question": "What decimal number does binary 0100 represent?",
        "answer": "4",
        "hints": [
            "Binary 0100 = 2^2 = 4."
        ],
        "solution": "Binary 0100 equals decimal 4."
    },
    {
        "id": "code_breaking_010",
        "title": "The Arithmetic Sequence Lock",
        "category": "code_breaking",
        "difficulty": "medium",
        "description": "🗝️ Recovered Notebook Page: Sequence: 4, 9, 14, 19, ?",
        "question": "What is the next number?",
        "answer": "24",
        "hints": [
            "Add +5 to each term.",
            "19 + 5 = 24."
        ],
        "solution": "Common difference is +5. 19 + 5 = 24."
    },
    {
        "id": "code_breaking_011",
        "title": "Mastermind Style Code Elimination",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "📂 Evidence Folder #7:\nCode is 4 digits.\n1-2-3-4 has 0 correct digits.\n5-6-7-8 has all 4 correct digits in exact order.",
        "question": "What is the code?",
        "answer": "5678",
        "hints": [
            "1-2-3-4 eliminated completely.",
            "5-6-7-8 contains all correct digits."
        ],
        "solution": "The code is 5678."
    },
    {
        "id": "code_breaking_012",
        "title": "The Matrix System Key",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "📄 Forensic Report #104:\nx + 2 = 6 (so x = 4)\ny - x = 1 (so y = 5)\nz = x + y (so z = 9)",
        "question": "Enter key as x-y-z:",
        "answer": "4-5-9",
        "hints": [
            "x = 6 - 2 = 4.",
            "y = 1 + 4 = 5.",
            "z = 4 + 5 = 9."
        ],
        "solution": "x=4, y=5, z=9. Key: 4-5-9."
    },
    {
        "id": "code_breaking_013",
        "title": "Modular Arithmetic Padlock",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "🔐 Encrypted USB Drive: Calculate (17 mod 5):",
        "question": "What is 17 modulo 5 (remainder of 17 / 5)?",
        "answer": "2",
        "hints": [
            "17 divided by 5 is 3 with remainder 2."
        ],
        "solution": "17 = 5 * 3 + 2. Remainder is 2."
    },
    {
        "id": "code_breaking_014",
        "title": "Multi-Layer Symmetric PIN",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "📜 Anonymous Letter: 4-digit code. Symmetrical (palindrome). First digit is 3. Second is 9.",
        "question": "What is the complete 4-digit code?",
        "answer": "3993",
        "hints": [
            "Symmetrical means digit 4 = digit 1 (3), digit 3 = digit 2 (9)."
        ],
        "solution": "3-9-9-3."
    },
    {
        "id": "code_breaking_015",
        "title": "The Double Shift Micro-Lock",
        "category": "code_breaking",
        "difficulty": "hard",
        "description": "📝 Witness Deposition: Shift letter 'A' forward by 2, then forward by 3.",
        "question": "What final letter is reached?",
        "answer": "F",
        "hints": [
            "A + 2 = C.",
            "C + 3 = F."
        ],
        "solution": "A -> C -> F."
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
        "description": "📝 Witness Deposition:\nWitness A: 'It poured rain heavily all night from 8 PM to 4 AM.'\nWitness B: 'I sat in the garden at 10 PM admiring the bright full moon in a completely clear sky.'\nWeather Log: Heavy downpour & storm all night.",
        "question": "Which witness is lying?",
        "answer": "WITNESS B",
        "hints": [
            "Compare Witness B's clear sky claim with the official Weather Log.",
            "Heavy rain all night makes seeing the moon in a clear sky impossible.",
            "Witness B lied about sitting outside under a clear sky."
        ],
        "solution": "Weather log confirms heavy rain all night. Witness B's claim of a clear full moon is a lie."
    },
    {
        "id": "witness_statements_002",
        "title": "The Clock Chimes Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "📂 Evidence Folder #7:\nWitness C: 'I heard the parlor grandfather clock chime 12 full times at 12:30 AM.'\nClockmaker Inspection: The parlor clock chimes once at half-past, and hour counts only at the top of the hour.",
        "question": "Which witness is lying?",
        "answer": "WITNESS C",
        "hints": [
            "Grandfather clocks chime once on half-hours.",
            "Witness C claims 12 chimes at 12:30 AM."
        ],
        "solution": "Grandfather clocks chime only once at half-hours. Witness C lied about hearing 12 chimes at 12:30."
    },
    {
        "id": "witness_statements_003",
        "title": "The Wall Reflection Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "📄 Forensic Report #104:\nWitness A: 'I stood in the hallway and saw the killer's face reflected in the brick wall mirror.'\nArchitecture Report: The hallway brick wall contains zero mirrors.",
        "question": "Which witness is lying?",
        "answer": "WITNESS A",
        "hints": [
            "There are no mirrors on the hallway brick wall."
        ],
        "solution": "Witness A claimed to see a reflection in a non-existent mirror."
    },
    {
        "id": "witness_statements_004",
        "title": "The Cold Tea Cup Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "📜 Anonymous Letter:\nWitness B: 'The victim poured steaming hot tea 1 minute before he died at 9:00 PM.'\nForensic Test: The tea cup on the desk was frozen solid with ice.",
        "question": "Which witness is lying?",
        "answer": "WITNESS B",
        "hints": [
            "Steaming tea cannot freeze solid in 1 minute."
        ],
        "solution": "Witness B's claim of steaming hot tea contradicts the frozen tea cup."
    },
    {
        "id": "witness_statements_005",
        "title": "The Shadow Direction Contradiction",
        "category": "witness_statements",
        "difficulty": "easy",
        "description": "🗝️ Recovered Notebook Page:\nWitness C: 'At high noon (12:00 PM) under the direct overhead sun, the killer's shadow stretched 50 feet due East.'",
        "question": "Which witness is lying?",
        "answer": "WITNESS C",
        "hints": [
            "Direct overhead noon sun casts minimal shadow directly below, not 50 ft East."
        ],
        "solution": "Overhead noon sun cannot cast a 50-foot shadow due East. Witness C lied."
    },
    {
        "id": "witness_statements_006",
        "title": "The Footstep Distance Contradiction",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "📻 Decoded Radio Transmission:\nWitness A: 'I heard the killer take 100 heavy paces walking down the 10-foot scullery hallway.'",
        "question": "Which witness is lying?",
        "answer": "WITNESS A",
        "hints": [
            "100 paces in a 10-foot hallway means each step is 1.2 inches long."
        ],
        "solution": "Taking 100 paces in a 10-foot hallway is absurd. Witness A lied."
    },
    {
        "id": "witness_statements_007",
        "title": "The Cold Motor Engine",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "🧩 Locked Filing Cabinet:\nWitness B: 'I just drove my motor car 50 miles at high speed, arriving at 9:00 PM.'\nDetective Inspection at 9:02 PM: The motor car engine block is freezing cold.",
        "question": "Which witness is lying?",
        "answer": "WITNESS B",
        "hints": [
            "Driving 50 miles leaves the engine block hot, not freezing cold."
        ],
        "solution": "A freshly driven engine is hot. Witness B's cold engine proves he lied."
    },
    {
        "id": "witness_statements_008",
        "title": "The Smoke Residue Contradiction",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "🔐 Encrypted USB Drive:\nWitness C: 'The victim smoked 3 cigars with me right before he died.'\nAutopsy Report: Zero tobacco smoke residue or carbon monoxide in victim's lungs.",
        "question": "Which witness is lying?",
        "answer": "WITNESS C",
        "hints": [
            "Autopsy proves victim inhaled no smoke."
        ],
        "solution": "Autopsy lung findings disprove Witness C's claim."
    },
    {
        "id": "witness_statements_009",
        "title": "The Telegram Timestamp Contradiction",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "📂 Evidence Folder #7:\nWitness A: 'I received the victim's telegram at 2:00 PM.'\nTelegraph Office Record: Telegram was dispatched at 4:00 PM.",
        "question": "Which witness is lying?",
        "answer": "WITNESS A",
        "hints": [
            "You cannot receive a telegram before it is sent."
        ],
        "solution": "Witness A claimed receipt 2 hours prior to dispatch."
    },
    {
        "id": "witness_statements_010",
        "title": "The Spectacles Vision Contradiction",
        "category": "witness_statements",
        "difficulty": "medium",
        "description": "📄 Forensic Report #104:\nWitness B (legally blind without thick glasses): 'I lost my glasses at noon, but at 10 PM in pitch darkness I clearly recognized the killer's facial mole from 100 yards away.'",
        "question": "Which witness is lying?",
        "answer": "WITNESS B",
        "hints": [
            "Blind without glasses + pitch darkness + 100 yards away."
        ],
        "solution": "Witness B's vision claim is physically impossible."
    },
    {
        "id": "witness_statements_011",
        "title": "The Sound Speed Delay Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "📜 Anonymous Letter:\nWitness C: 'I saw the gunshot flash on the hill 2 miles away and heard the bang at the exact same millisecond.'",
        "question": "Which witness is lying?",
        "answer": "WITNESS C",
        "hints": [
            "Sound travels ~1 mile per 5 seconds. 2 miles takes ~10 seconds."
        ],
        "solution": "Sound delay over 2 miles is ~10 seconds. Witness C lied."
    },
    {
        "id": "witness_statements_012",
        "title": "The Low Tide Landing Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "🗝️ Recovered Notebook Page:\nWitness A: 'I docked my deep-draft schooner at the high-water pier at 3:00 PM.'\nHarbor Tide Table: 3:00 PM was the lowest ebb tide of the year (pier was completely dry mud).",
        "question": "Which witness is lying?",
        "answer": "WITNESS A",
        "hints": [
            "Deep draft ships cannot dock at dry mud low tide."
        ],
        "solution": "Witness A lied about docking at high tide when harbor was dry mud."
    },
    {
        "id": "witness_statements_013",
        "title": "The Courtyard Echo Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "📝 Witness Deposition:\nWitness B: 'The gun fired from the open West field, but the sound echoed off the West open field.'\nAcoustics Report: Open fields produce zero echoes; echoes require solid walls.",
        "question": "Which witness is lying?",
        "answer": "WITNESS B",
        "hints": [
            "Echoes require a reflecting surface."
        ],
        "solution": "Witness B claimed an echo from an open field."
    },
    {
        "id": "witness_statements_014",
        "title": "The Sodium Gaslamp Color Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "📻 Decoded Radio Transmission:\nWitness C: 'Under the monochromatic yellow sodium gaslamp, I clearly distinguished the killer's bright red ribbon from a green ribbon.'",
        "question": "Which witness is lying?",
        "answer": "WITNESS C",
        "hints": [
            "Monochromatic sodium light renders red and green as identical dark gray."
        ],
        "solution": "Color discrimination under monochromatic light is impossible. Witness C lied."
    },
    {
        "id": "witness_statements_015",
        "title": "The Mirror Reading Contradiction",
        "category": "witness_statements",
        "difficulty": "hard",
        "description": "🧩 Locked Filing Cabinet:\nWitness A: 'I read the regular non-reversed handwriting on the note reflected in the mirror across the room.'",
        "question": "Which witness is lying?",
        "answer": "WITNESS A",
        "hints": [
            "Handwriting reflected in a mirror appears reversed (mirror writing)."
        ],
        "solution": "Reflected text is mirrored/reversed. Witness A lied."
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
        "description": "📄 Forensic Report #104:\nBlood sample from weapon: Type AB negative.\nSuspect 1: Type O positive\nSuspect 2: Type A positive\nSuspect 3: Type AB negative",
        "question": "Which suspect matches the blood sample?",
        "answer": "SUSPECT 3",
        "hints": [
            "Compare blood type AB negative to suspects.",
            "Suspect 3 is Type AB negative."
        ],
        "solution": "Suspect 3 matches the AB negative blood found on the murder weapon."
    },
    {
        "id": "evidence_analysis_002",
        "title": "Shoe Size Footprint Analysis",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "📂 Evidence Folder #7:\nCrime scene mud footprint: Size 11.\nSuspect A: Size 8\nSuspect B: Size 9\nSuspect C: Size 11",
        "question": "Which suspect matches the crime scene footprint?",
        "answer": "SUSPECT C",
        "hints": [
            "Footprint size is 11.",
            "Suspect C wears size 11."
        ],
        "solution": "Suspect C matches size 11."
    },
    {
        "id": "evidence_analysis_003",
        "title": "Rigor Mortis Time of Death",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "🗝️ Recovered Notebook Page:\nRigor mortis takes 12 hours to fully set.\nBody discovered at 8:00 AM with full rigor mortis.",
        "question": "At what time the previous evening did death occur?",
        "answer": "8:00 PM",
        "hints": [
            "8:00 AM minus 12 hours = 8:00 PM."
        ],
        "solution": "Death occurred 12 hours prior at 8:00 PM."
    },
    {
        "id": "evidence_analysis_004",
        "title": "Fingerprint Pattern Matching",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "📜 Anonymous Letter:\nWeapon print: Whorl pattern.\nSuspect 1: Arch\nSuspect 2: Loop\nSuspect 3: Whorl",
        "question": "Which suspect matches the print?",
        "answer": "SUSPECT 3",
        "hints": [
            "Whorl pattern matches Suspect 3."
        ],
        "solution": "Suspect 3 matches Whorl pattern."
    },
    {
        "id": "evidence_analysis_005",
        "title": "Ink Chromatography Analysis",
        "category": "evidence_analysis",
        "difficulty": "easy",
        "description": "📝 Witness Deposition:\nRansom note ink: Water-soluble black ink.\nSuspect A pen: Iron gall ink\nSuspect B pen: Water-soluble black ink\nSuspect C pen: Blue ballpoint",
        "question": "Which suspect's pen was used?",
        "answer": "SUSPECT B",
        "hints": [
            "Water-soluble black ink matches Suspect B."
        ],
        "solution": "Suspect B matches water-soluble black ink."
    },
    {
        "id": "evidence_analysis_006",
        "title": "Gunpowder Residue Location",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "📻 Decoded Radio Transmission:\nResidue found on right hand only.\nSuspect A: Left-handed, residue on left hand\nSuspect B: Right-handed, residue on right hand\nSuspect C: No residue",
        "question": "Which suspect fired the weapon?",
        "answer": "SUSPECT B",
        "hints": [
            "Right hand residue matches Suspect B."
        ],
        "solution": "Suspect B matches right hand gunpowder residue."
    },
    {
        "id": "evidence_analysis_007",
        "title": "Soil Analysis from Boots",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "🧩 Locked Filing Cabinet:\nCrime scene soil: Red clay.\nSuspect 1 boots: White chalk\nSuspect 2 boots: Red clay\nSuspect 3 boots: Clean",
        "question": "Which suspect walked through the crime scene?",
        "answer": "SUSPECT 2",
        "hints": [
            "Red clay soil matches Suspect 2."
        ],
        "solution": "Suspect 2 matches red clay soil."
    },
    {
        "id": "evidence_analysis_008",
        "title": "Arsenic Poison Dosage",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "🔐 Encrypted USB Drive:\nFatal arsenic dose: 100mg.\nAutopsy findings: 150mg arsenic in stomach, ingested 2 hours prior during dinner served by Chef.",
        "question": "Who served the fatal poisoned meal?",
        "answer": "CHEF",
        "hints": [
            "Poison ingested during dinner served by Chef."
        ],
        "solution": "Chef served the meal containing fatal arsenic."
    },
    {
        "id": "evidence_analysis_009",
        "title": "Fabric Fiber Matching",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "📂 Evidence Folder #7:\nWindow latch snagged fiber: Green velvet.\nSuspect A: Tweed suit\nSuspect B: Green velvet jacket\nSuspect C: Silk gown",
        "question": "Which suspect's clothing matches the fiber?",
        "answer": "SUSPECT B",
        "hints": [
            "Green velvet jacket matches Suspect B."
        ],
        "solution": "Suspect B matches green velvet fiber."
    },
    {
        "id": "evidence_analysis_010",
        "title": "Glass Splatter Direction",
        "category": "evidence_analysis",
        "difficulty": "medium",
        "description": "📄 Forensic Report #104:\nBroken glass fragments were found entirely INSIDE the study room.",
        "question": "Was the window broken from OUTSIDE or INSIDE?",
        "answer": "OUTSIDE",
        "hints": [
            "Impact force pushes glass fragments in the direction of blow (into the room)."
        ],
        "solution": "Glass inside room means force came from OUTSIDE."
    },
    {
        "id": "evidence_analysis_011",
        "title": "Triple Factor Forensic Elimination",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "🗝️ Recovered Notebook Page:\nCrime scene evidence: Blood A+, Footprint Size 10, Tweed fiber.\nSuspect 1: Blood A+, Size 10, Tweed fiber\nSuspect 2: Blood B+, Size 10, Tweed fiber\nSuspect 3: Blood A+, Size 8, Silk fiber",
        "question": "Which suspect matches ALL three evidence factors?",
        "answer": "SUSPECT 1",
        "hints": [
            "Suspect 1 has A+, Size 10, Tweed."
        ],
        "solution": "Suspect 1 matches all three forensic criteria."
    },
    {
        "id": "evidence_analysis_012",
        "title": "Tox Peak Reaction Timing",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "📜 Anonymous Letter:\nStrychnine peak toxicity occurs 1 hour after ingestion.\nVictim died of peak toxicity at 10:00 PM.",
        "question": "At what time was the poison ingested?",
        "answer": "9:00 PM",
        "hints": [
            "10:00 PM minus 1 hour = 9:00 PM."
        ],
        "solution": "Poison ingested at 9:00 PM."
    },
    {
        "id": "evidence_analysis_013",
        "title": "Ballistic Rifling Grooves",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "📝 Witness Deposition:\nBullet recovered: Left-hand twist rifling.\nGun A: Right-hand twist\nGun B: Left-hand twist",
        "question": "Which gun fired the fatal shot?",
        "answer": "GUN B",
        "hints": [
            "Left-hand twist matches Gun B."
        ],
        "solution": "Gun B matches left-hand twist rifling."
    },
    {
        "id": "evidence_analysis_014",
        "title": "Dental Bite Mark Spacing",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "📻 Decoded Radio Transmission:\nBite mark on apple shows missing left upper canine.\nSuspect X: All teeth intact\nSuspect Y: Missing left upper canine",
        "question": "Which suspect bit the apple?",
        "answer": "SUSPECT Y",
        "hints": [
            "Suspect Y missing left upper canine."
        ],
        "solution": "Suspect Y matches dental impression."
    },
    {
        "id": "evidence_analysis_015",
        "title": "Comprehensive Lab Summary Match",
        "category": "evidence_analysis",
        "difficulty": "hard",
        "description": "🧩 Locked Filing Cabinet:\nLab report: Fingerprint Loop, Footprint Size 9, Blood O negative.\nSuspect Alpha: Loop, Size 9, O negative\nSuspect Beta: Whorl, Size 11, AB positive",
        "question": "Which suspect matches the lab report summary?",
        "answer": "SUSPECT ALPHA",
        "hints": [
            "Suspect Alpha matches Loop, Size 9, O-."
        ],
        "solution": "Suspect Alpha matches the lab report."
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
            "schema_version": "1.0",
            "id": p["id"],
            "title": p["title"],
            "category": p["category"],
            "difficulty": p["difficulty"],
            "description": p["description"],
            "question": p["question"],
            "answer": p["answer"],
            "hints": p["hints"],
            "solution": p["solution"]
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    print("\nPuzzles created per category:")
    for cat, count in sorted(counts.items()):
        print(f" - {cat}: {count} puzzles")
    
    print("\nAll 120 puzzle JSON files generated successfully!")

if __name__ == "__main__":
    main()
