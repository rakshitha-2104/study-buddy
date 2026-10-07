// All fixed interface text lives here, one block per language.
// To add a language: add a block with the same keys and one entry in LANGUAGES.
export const LANGUAGES = [
  { code: "kn", label: "ಕನ್ನಡ" },
  { code: "te", label: "తెలుగు" },
  { code: "hi", label: "हिन्दी" },
  { code: "ml", label: "മലയാളം" },
  { code: "ta", label: "தமிழ்" },
  { code: "en", label: "English" },
];

export const T = {
  en: { welcome: "Welcome!", name: "Name", id: "Student ID", password: "Password (min 6)", login: "Login", register: "Register",
    subjects: "Subjects", askAi: "Your Study Buddy", typeQ: "Type your question...", send: "Send", unit: "Unit",
    startQuiz: "Start Quiz", next: "Next", finish: "Finish", score: "Score", dashboard: "My Progress", logout: "Logout",
    back: "Back", easy: "Easy", medium: "Medium", hard: "Hard", excellent: "Excellent! Keep shining!", good: "Good job! Almost there!",
    practice: "Keep practising, you can do it!", gaps: "Needs more practice", noData: "Take a quiz to see your graph", error: "Something went wrong, try again",
    noTrans: "Translation is not available right now, showing English.",
    greet: "Hi! Ask me any doubt from your subjects.", notFound: "I don't know that one yet. Try asking about:", revise: "You found this unit tricky. Revise it once more!" },

  kn: { welcome: "ಸ್ವಾಗತ!", name: "ಹೆಸರು", id: "ವಿದ್ಯಾರ್ಥಿ ಐಡಿ", password: "ಪಾಸ್‌ವರ್ಡ್ (ಕನಿಷ್ಠ 6)", login: "ಲಾಗಿನ್", register: "ನೋಂದಣಿ",
    subjects: "ವಿಷಯಗಳು", askAi: "ನಿಮ್ಮ ಸ್ಟಡಿ ಬಡ್ಡಿ", typeQ: "ನಿಮ್ಮ ಪ್ರಶ್ನೆ ಬರೆಯಿರಿ...", send: "ಕಳುಹಿಸಿ", unit: "ಘಟಕ",
    startQuiz: "ರಸಪ್ರಶ್ನೆ ಆರಂಭಿಸಿ", next: "ಮುಂದೆ", finish: "ಮುಗಿಸಿ", score: "ಅಂಕ", dashboard: "ನನ್ನ ಪ್ರಗತಿ", logout: "ಲಾಗ್ ಔಟ್",
    back: "ಹಿಂದೆ", easy: "ಸುಲಭ", medium: "ಮಧ್ಯಮ", hard: "ಕಠಿಣ", excellent: "ಅದ್ಭುತ! ಹೀಗೆಯೇ ಮುಂದುವರಿಸಿ!", good: "ಚೆನ್ನಾಗಿದೆ! ಇನ್ನೊಂದು ಸ್ವಲ್ಪ!",
    practice: "ಅಭ್ಯಾಸ ಮುಂದುವರಿಸಿ, ನೀವು ಮಾಡಬಲ್ಲಿರಿ!", gaps: "ಹೆಚ್ಚು ಅಭ್ಯಾಸ ಬೇಕು", noData: "ಗ್ರಾಫ್ ನೋಡಲು ರಸಪ್ರಶ್ನೆ ಬರೆಯಿರಿ", error: "ಏನೋ ತಪ್ಪಾಯಿತು, ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ",
    noTrans: "ಅನುವಾದ ಈಗ ಲಭ್ಯವಿಲ್ಲ, ಇಂಗ್ಲಿಷ್ ತೋರಿಸಲಾಗುತ್ತಿದೆ.",
    greet: "ನಮಸ್ಕಾರ! ನಿಮ್ಮ ವಿಷಯಗಳ ಯಾವುದೇ ಸಂದೇಹ ಕೇಳಿ.", notFound: "ಇದರ ಬಗ್ಗೆ ನನಗೆ ಇನ್ನೂ ಗೊತ್ತಿಲ್ಲ. ಇವುಗಳ ಬಗ್ಗೆ ಕೇಳಿ:", revise: "ಈ ಘಟಕ ನಿಮಗೆ ಕಷ್ಟವಾಗಿತ್ತು. ಇನ್ನೊಮ್ಮೆ ಓದಿ!" },
  te: { welcome: "స్వాగతం!", name: "పేరు", id: "విద్యార్థి ఐడీ", password: "పాస్‌వర్డ్ (కనీసం 6)", login: "లాగిన్", register: "నమోదు",
    subjects: "సబ్జెక్టులు", askAi: "మీ స్టడీ బడ్డీ", typeQ: "మీ ప్రశ్న రాయండి...", send: "పంపండి", unit: "యూనిట్",
    startQuiz: "క్విజ్ ప్రారంభించండి", next: "తదుపరి", finish: "ముగించు", score: "మార్కులు", dashboard: "నా ప్రగతి", logout: "లాగ్ అవుట్",
    back: "వెనుకకు", easy: "సులభం", medium: "మధ్యస్థం", hard: "కఠినం", excellent: "అద్భుతం! ఇలాగే కొనసాగించండి!", good: "బాగుంది! ఇంకొంచెం!",
    practice: "సాధన కొనసాగించండి, మీరు చేయగలరు!", gaps: "ఇంకా సాధన అవసరం", noData: "గ్రాఫ్ చూడటానికి క్విజ్ రాయండి", error: "ఏదో తప్పు జరిగింది, మళ్లీ ప్రయత్నించండి",
    noTrans: "అనువాదం ప్రస్తుతం అందుబాటులో లేదు, ఇంగ్లీష్ చూపిస్తున్నాం.",
    greet: "హాయ్! మీ సబ్జెక్టుల్లో ఏ సందేహమైనా అడగండి.", notFound: "దీని గురించి నాకు ఇంకా తెలియదు. వీటి గురించి అడగండి:", revise: "ఈ యూనిట్ మీకు కష్టంగా అనిపించింది. మరోసారి చదవండి!" },
  hi: { welcome: "स्वागत है!", name: "नाम", id: "छात्र आईडी", password: "पासवर्ड (कम से कम 6)", login: "लॉगिन", register: "रजिस्टर",
    subjects: "विषय", askAi: "आपका स्टडी बडी", typeQ: "अपना सवाल लिखें...", send: "भेजें", unit: "इकाई",
    startQuiz: "क्विज़ शुरू करें", next: "आगे", finish: "समाप्त", score: "अंक", dashboard: "मेरी प्रगति", logout: "लॉग आउट",
    back: "वापस", easy: "आसान", medium: "मध्यम", hard: "कठिन", excellent: "शानदार! ऐसे ही चमकते रहो!", good: "बढ़िया! बस थोड़ा और!",
    practice: "अभ्यास जारी रखें, आप कर सकते हैं!", gaps: "और अभ्यास चाहिए", noData: "ग्राफ देखने के लिए क्विज़ दें", error: "कुछ गड़बड़ हुई, फिर कोशिश करें",
    noTrans: "अनुवाद अभी उपलब्ध नहीं है, अंग्रेज़ी दिखाई जा रही है।",
    greet: "नमस्ते! अपने विषयों का कोई भी सवाल पूछिए।", notFound: "यह मुझे अभी नहीं आता। इनके बारे में पूछिए:", revise: "यह इकाई आपको कठिन लगी थी। एक बार फिर पढ़ें!" },
  ml: { welcome: "സ്വാഗതം!", name: "പേര്", id: "വിദ്യാർത്ഥി ഐഡി", password: "പാസ്‌വേഡ് (കുറഞ്ഞത് 6)", login: "ലോഗിൻ", register: "രജിസ്റ്റർ",
    subjects: "വിഷയങ്ങൾ", askAi: "നിങ്ങളുടെ സ്റ്റഡി ബഡ്ഡി", typeQ: "നിങ്ങളുടെ ചോദ്യം എഴുതൂ...", send: "അയയ്ക്കുക", unit: "യൂണിറ്റ്",
    startQuiz: "ക്വിസ് തുടങ്ങൂ", next: "അടുത്തത്", finish: "പൂർത്തിയാക്കുക", score: "സ്കോർ", dashboard: "എന്റെ പുരോഗതി", logout: "ലോഗ് ഔട്ട്",
    back: "പിന്നോട്ട്", easy: "എളുപ്പം", medium: "ഇടത്തരം", hard: "കഠിനം", excellent: "കൊള്ളാം! ഇതുപോലെ തുടരൂ!", good: "നന്നായി! ഇനി കുറച്ചുകൂടി!",
    practice: "പരിശീലനം തുടരൂ, നിങ്ങൾക്ക് സാധിക്കും!", gaps: "കൂടുതൽ പരിശീലനം വേണം", noData: "ഗ്രാഫ് കാണാൻ ഒരു ക്വിസ് എഴുതൂ", error: "എന്തോ പിശക് സംഭവിച്ചു, വീണ്ടും ശ്രമിക്കൂ",
    noTrans: "വിവർത്തനം ഇപ്പോൾ ലഭ്യമല്ല, ഇംഗ്ലീഷ് കാണിക്കുന്നു.",
    greet: "ഹായ്! നിങ്ങളുടെ വിഷയങ്ങളിലെ ഏത് സംശയവും ചോദിക്കൂ.", notFound: "ഇത് എനിക്ക് ഇതുവരെ അറിയില്ല. ഇവയെക്കുറിച്ച് ചോദിക്കൂ:", revise: "ഈ യൂണിറ്റ് നിങ്ങൾക്ക് ബുദ്ധിമുട്ടായിരുന്നു. ഒരിക്കൽ കൂടി പഠിക്കൂ!" },
  ta: { welcome: "வரவேற்கிறோம்!", name: "பெயர்", id: "மாணவர் அடையாள எண்", password: "கடவுச்சொல் (குறைந்தது 6)", login: "உள்நுழை", register: "பதிவு செய்",
    subjects: "பாடங்கள்", askAi: "உங்கள் ஸ்டடி பட்டி", typeQ: "உங்கள் கேள்வியை எழுதுங்கள்...", send: "அனுப்பு", unit: "அலகு",
    startQuiz: "வினாடி வினா தொடங்கு", next: "அடுத்து", finish: "முடி", score: "மதிப்பெண்", dashboard: "என் முன்னேற்றம்", logout: "வெளியேறு",
    back: "பின்செல்", easy: "எளிது", medium: "நடுத்தரம்", hard: "கடினம்", excellent: "அருமை! இப்படியே தொடருங்கள்!", good: "நன்று! இன்னும் கொஞ்சம்!",
    practice: "பயிற்சியைத் தொடருங்கள், உங்களால் முடியும்!", gaps: "இன்னும் பயிற்சி தேவை", noData: "வரைபடம் பார்க்க ஒரு வினாடி வினா எழுதுங்கள்", error: "ஏதோ தவறு நடந்தது, மீண்டும் முயலுங்கள்",
    noTrans: "மொழிபெயர்ப்பு இப்போது கிடைக்கவில்லை, ஆங்கிலம் காட்டப்படுகிறது.",
    greet: "வணக்கம்! உங்கள் பாடங்களில் எந்த சந்தேகத்தையும் கேளுங்கள்.", notFound: "இது எனக்கு இன்னும் தெரியாது. இவற்றைப் பற்றி கேளுங்கள்:", revise: "இந்த அலகு உங்களுக்குக் கடினமாக இருந்தது. மீண்டும் படியுங்கள்!" },
};

// Subject names shown in the selected language (technical names stay recognisable).
export const SUBJECT_NAMES = {
  cn:     { en: "Computer Networks", kn: "ಕಂಪ್ಯೂಟರ್ ನೆಟ್‌ವರ್ಕ್ಸ್", te: "కంప్యూటర్ నెట్‌వర్క్స్", hi: "कंप्यूटर नेटवर्क", ml: "കമ്പ്യൂട്ടർ നെറ്റ്‌വർക്ക്സ്", ta: "கணினி வலையமைப்புகள்" },
  dbms:   { en: "DBMS", kn: "DBMS", te: "DBMS", hi: "DBMS", ml: "DBMS", ta: "DBMS" },
  python: { en: "Python", kn: "ಪೈಥಾನ್", te: "పైథాన్", hi: "पाइथन", ml: "പൈത്തൺ", ta: "பைதான்" },
  java:   { en: "Java", kn: "ಜಾವಾ", te: "జావా", hi: "जावा", ml: "ജാവ", ta: "ஜாவா" },
  c:      { en: "C Programming", kn: "C ಪ್ರೋಗ್ರಾಮಿಂಗ್", te: "C ప్రోగ్రామింగ్", hi: "C प्रोग्रामिंग", ml: "C പ്രോഗ്രാമിംഗ്", ta: "C நிரலாக்கம்" },
  cyber:  { en: "Cyber Security", kn: "ಸೈಬರ್ ಭದ್ರತೆ", te: "సైబర్ భద్రత", hi: "साइबर सुरक्षा", ml: "സൈബർ സുരക്ഷ", ta: "இணையப் பாதுகாப்பு" },
};

export const SUBJECT_EMOJI = { cn: "🌐", dbms: "🗄️", python: "🐍", java: "☕", c: "⚙️", cyber: "🔐" };