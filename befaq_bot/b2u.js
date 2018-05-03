function Insert(field, text)
{
    if (document.selection) 
    {
        field.focus();
        sel = document.selection.createRange();
        sel.text = text;
        sel.collapse(true);
        sel.select();
    }

    else if (field.selectionStart || field.selectionStart == '0')
    {

        
        var startPos = field.selectionStart;
        var endPos = field.selectionEnd;
        var scrollTop = field.scrollTop;
        startPos = (startPos == -1 ? field.value.length : startPos );
        field.value = field.value.substring(0, startPos)
            + text
            + field.value.substring(endPos, field.value.length);
        field.focus();
        field.selectionStart = startPos + text.length;
        field.selectionEnd = startPos + text.length;
        field.scrollTop = scrollTop;
    }
    else
    {
        var scrollTop = field.scrollTop;
        field.value += value;
        field.focus();
        field.scrollTop = scrollTop;
    }

} 

function RemoveNInsert(field, value, len) 
{
    if (document.selection) 
    {
        field.focus();
        sel = document.selection.createRange();
        if (field.value.length >= len)
            {           
            sel.moveStart('character', -1*(len));   
            }
        sel.text = value;
        sel.collapse(true);
        sel.select();
        }

    else if (field.selectionStart || field.selectionStart == 0) {
        field.focus();
        var startPos = field.selectionStart-len;
        var endPos = field.selectionEnd;
        var scrollTop = field.scrollTop;
        startPos = (startPos == -1 ? field.value.length : startPos );
        field.value = field.value.substring(0, startPos)
        + value
        + field.value.substring(endPos, field.value.length);
        field.focus();
        field.selectionStart = startPos + value.length;
        field.selectionEnd = startPos + value.length;
        field.scrollTop = scrollTop;
    } else {
        var scrollTop = field.scrollTop;
        field.value += value;
        field.focus();
        field.scrollTop = scrollTop;
    }

} 

function capsDetect( e )
{
    if( !e ) e = window.event;
    if( !e ) return false;
    //what (case sensitive in good browsers) key was pressed
    var theKey = e.which ? e.which : ( e.keyCode ? e.keyCode : ( e.charCode ? e.charCode : 0 ) );
    //was the shift key was pressed
    var theShift = e.shiftKey || ( e.modifiers && ( e.modifiers & 4 ) ); //bitWise AND
    //if upper case, check if shift is not pressed. if lower case, check if shift is pressed
    return ( ( theKey > 64 && theKey < 91 && !theShift ) || ( theKey > 96 && theKey < 123 && theShift ) );
}

function HideDIV(id)
{
    //safe function to hide an element with a specified id
    if (document.getElementById) { // DOM3 = IE5, NS6
        document.getElementById(id).style.display = 'none';
    }
    else {
        if (document.layers) { // Netscape 4
            document.id.display = 'none';
        }
        else { // IE 4
            document.all.id.style.display = 'none';
        }
    }
} // end function hidediv



function ShowDIV(id)
{
    //safe function to show an element with a specified id
          
    if (document.getElementById) { // DOM3 = IE5, NS6
        document.getElementById(id).style.display = 'block';
    }
    else {
        if (document.layers) { // Netscape 4
            document.id.display = 'block';
        }
        else { // IE 4
            document.all.id.style.display = 'block';
        }
    }
} // end function showdiv

function IsBanglaDigit(CUni)
{
    if(CUni=='০' || CUni=='১'
    || CUni=='২' || CUni=='৩'
    || CUni=='৪' || CUni=='৫'
    || CUni=='৬' || CUni=='৭'
    || CUni=='৮' || CUni=='৯')
        return true;

    return false;
} // end function IsBanglaDigit

function IsBanglaPreKar(CUni)
{
    if(CUni=='ি' || CUni=='ৈ' 
    || CUni=='ে' )
        return true;
    
    return false;
} // end function IsBanglaPreKar

function IsBanglaPostKar(CUni)
{
    if(CUni == 'া' || CUni=='ো'
    || CUni=='ৌ' || CUni=='ৗ' || CUni=='ু'
    || CUni=='ূ' || CUni=='ী'
    || CUni=='ৃ')
        return true;
    return false;
} // end function IsBanglaPostKar

function IsBanglaKar(CUni)
{
    if(IsBanglaPreKar(CUni) || IsBanglaPostKar(CUni) )
        return true;
    return false;

} // end function IsBanglaKar

function IsBanglaBanjonborno(CUni)
{
    if(CUni=='ক' || CUni=='খ' || CUni=='গ' || CUni=='ঘ' || CUni=='ঙ' 
        || CUni=='চ' || CUni=='ছ' || CUni=='জ' || CUni=='ঝ' || CUni=='ঞ' 
        || CUni=='ট' || CUni=='ঠ' || CUni=='ড' || CUni=='ঢ' || CUni=='ণ'
        || CUni=='ত' || CUni=='থ' || CUni=='দ' || CUni=='ধ' || CUni=='ন'
        || CUni=='প' || CUni=='ফ' || CUni=='ব' || CUni=='ভ' || CUni=='ম'
        || CUni=='শ' || CUni=='ষ' || CUni=='স' || CUni=='হ' 
    || CUni=='য' || CUni=='র' || CUni=='ল' || CUni=='য়' 
    || CUni=='ং' || CUni=='ঃ' || CUni=='ঁ'
    || CUni=='ৎ')
        return true;

    return false;
} // end function IsBanglaBanjonborno

function IsBanglaSoroborno(CUni)
{
    if(CUni == 'অ' || CUni=='আ'
    || CUni=='ই' || CUni=='ঈ'
    || CUni=='উ' || CUni=='ঊ'
    || CUni=='ঋ' || CUni=='ঌ'
    || CUni=='এ' || CUni=='ঐ' 
    || CUni=='ও' || CUni=='ঔ' )
        return true;

    return false;
} // end function IsBanglaSoroborno

function IsBanglaNukta(CUni)
{
    if(CUni=='ং' || CUni=='ঃ' || CUni=='ঁ')
        return true;

    return false;

} // end function IsBanglaNukta

function IsBanglaFola(CUni)
{
    if(CUni=="্য" || CUni=="্র")
        return true;

    return false;
} // end function IsBanglaFola

function IsBanglaHalant(CUni)
{
    if(CUni=='্')
        return true;

    return false;
} // end function IsBanglaHalant
function IsBangla(CUni)
{
    if(IsBanglaDigit(CUni) || IsBanglaKar(CUni) ||
    IsBanglaBanjonborno(CUni) || IsBanglaSoroborno(CUni) ||
    IsBanglaNukta(CUni) || IsBanglaFola(CUni) || IsBanglaHalant(CUni))
        return true;

    return false;
} // end function IsBangla
function IsASCII(CH)
{
    if(CH >= 0 && CH< 128)
        return true;

    return false;
} // end function IsBangla

function IsSpace(C)
{
    if( C==' ' ||  C=='\t' || C=='\n'
    ||  C=='\r')
        return true;

    return false;
} // end function IsSpace

function MapKarToSorborno(CUni)
{
    var CSorborno = CUni;
    if(CUni=='া')
        CSorborno = 'আ';
    else if(CUni=='ি')
        CSorborno = 'ই';
    else if(CUni=='ী')
        CSorborno = 'ঈ';
    else if(CUni=='ু')
        CSorborno = 'উ';
    else if(CUni=='ূ')
        CSorborno = 'ঊ';
    else if(CUni=='ৃ')
        CSorborno = 'ঋ';
    else if(CUni=='ে')
        CSorborno = 'এ';
    else if(CUni=='ৈ')
        CSorborno = 'ঐ';
    else if(CUni=='ো')
        CSorborno = 'ও';
    else if(CUni=="ো")
        CSorborno = 'ও';
    else if(CUni=='ৌ')
        CSorborno = 'ঔ';
    else if(CUni=="ৌ")
        CSorborno = 'ঔ';

    return CSorborno;
} // end function MapKarToSorborno

function MapSorbornoToKar(CUni)
{
    var CKar = CUni;
    if(CUni=='আ')
        CKar = 'া';
    else if(CUni=='ই')
        CKar = 'ি';
    else if(CUni=='ঈ')
        CKar = 'ী';
    else if(CUni=='উ')
        CKar = 'ু';
    else if(CUni=='ঊ')
        CKar = 'ূ';
    else if(CUni=='ঋ')
        CKar = 'ৃ';
    else if(CUni=='এ')
        CKar = 'ে';
    else if(CUni=='ঐ')
        CKar = 'ৈ';
    else if(CUni=='ও')
        CKar = 'ো';
    else if(CUni=='ঔ')
        CKar = 'ৌ';

    return CKar;
} // end function MapSorbornoToKar

/**bijoy ekushey and bayanno pro**/
var bijoy_string_conversion_map = {
    // <JUKTAKHKHOR>
    "i¨":"র‌্য",
    "ª¨":"্র্য",
    "°":"ক্ক",
    "±":"ক্ট",
    "³":"ক্ত",
    "K¡":"ক্ব",
    "¯Œ":"স্ক্র",
    "µ":"ক্র",
    "K¬":"ক্ল",
    "ÿ":"ক্ষ",  
    "•":"ক্স",
    "¸":"গু",
    "»":"গ্ধ",
    "Mœ":"গ্ন",
    "M¥":"গ্ম",
    "Mø":"গ্ল",
    "¼":"ঙ্ক",
    "•¶":"ঙ্ক্ষ",
    "•L":"ঙ্খ",
    "½":"ঙ্গ",
    "•N":"ঙ্ঘ",
    "•":"ক্স",
    "”P":"চ্চ",
    "”Q":"চ্ছ",
    "”Q¡":"চ্ছ্ব",
    "”T":"চ্ঞ",
    "¾¡":"জ্জ্ব",
    "¾":"জ্জ",
    "À":"জ্ঝ",
    "Á":"জ্ঞ",
    "R¡":"জ্ব",
    "Â":"ঞ্চ",
    "Ã":"ঞ্ছ",
    "Ä":"ঞ্জ",
    "Å":"ঞ্ঝ",
    "Æ":"ট্ট",
    "U¡":"ট্ব",
    "U¥":"ট্ম",
    "Ç":"ড্ড",
    "È":"ণ্ট",
    "É":"ণ্ঠ",
    "Ý":"ন্স",
    "Ð":"ণ্ড",
    "š‘":"ন্তু",
    "Y^":"ণ্ব",
    "Ë":"ত্ত",
    "Ë¡":"ত্ত্ব",
    "Ì":"ত্থ",
    "Z¥":"ত্ম",
    "šÍ¡":"ন্ত্ব",
    "Z¡":"ত্ব",
    "Î":"ত্র",
    "_¡":"থ্ব",
    "˜M":"দ্গ",
    "˜N":"দ্ঘ",
    "Ï":"দ্দ",
    "×":"দ্ধ",
    "˜¡":"দ্ব",
    "Ø":"দ্ব",
    "™¢":"দ্ভ",
    "Ù":"দ্ম",
    "`ªæ":"দ্রু",
    "aŸ":"ধ্ব",
    "a¥":"ধ্ম",
    "›U":"ন্ট",
    "Ú":"ন্ঠ",
    "Û":"ন্ড",
    "šÍ":"ন্ত",
    "šÍ":"ন্ত",
    "š¿":"ন্ত্র",
    "š’":"ন্থ",
    "›`":"ন্দ",
    "›Ø":"ন্দ্ব",
    "Ü":"ন্ধ",
    "bœ":"ন্ন",
    "š^":"ন্ব",
    "b¥":"ন্ম",
    "Þ":"প্ট",
    "ß":"প্ত",
    "cœ":"প্ন",
    "à":"প্প",
    "cø":"প্ল",
    "cø":"প্ল",
    "á":"প্স",
    "d¬":"ফ্ল",
    "â":"ব্জ",
    "ã":"ব্দ",
    "ä":"ব্ধ",
    "eŸ":"ব্ব",
    "eø":"ব্ল",
    "å":"ভ্র",
    "gœ":"ম্ন",
    "¤ú":"ম্প",
    "ç":"ম্ফ",
    "¤\\^":"ম্ব", //ম্ব ¤\\^ //¤^
    "¤¢":"ম্ভ",
    "¤£":"ম্ভ্র",
    "¤§":"ম্ম",
    "¤ø":"ম্ল", 
    "iæ":"রু",
    "iæ":"রু",
    "iƒ":"রূ",
    "é":"ল্ক",
    "ê":"ল্গ",
    "ë":"ল্ট",
    "ì":"ল্ড",
    "í":"ল্প",
    "î":"ল্ফ",
    "j¦":"ল্ব",
    "j¥":"ল্ম",
    "jø":"ল্ল", 
    "ï":"শু",
    "ð":"শ্চ",
    "kœ":"শ্ন",
    "k¦":"শ্ব",
    "k¥":"শ্ম",
    "kø":"শ্ল",
    "®‹":"ষ্ক",
    "®Œ":"ষ্ক্র",
    "ó":"ষ্ট",
    "ô":"ষ্ঠ",
    "ò":"ষ্ণ",
    "®ú":"ষ্প",
    "õ":"ষ্ফ",
    "®§":"ষ্ম",
    "¯‹":"স্ক",
    "÷":"স্ট",
    "ö":"স্খ",
    "¯Í":"স্ত",
    "¯‘":"স্তু",
    "¯¿":"স্ত্র",
    "¯’":"স্থ",
    "mœ":"স্ন",
    "¯ú":"স্প",
    "ù":"স্ফ",
    "¯^":"স্ব",
    "¯§":"স্ম",
    "mø":"স্ল",
    "û":"হু",
    "nè":"হ্ণ",
    "ý":"হ্ন",
    "þ":"হ্ম",
    "n¬":"হ্ল",
    "ü":"হৃ",
    "©":"র্",

    // <VOWELS>
    "Av":"আ",
    "A":"অ",
    "B":"ই",
    "C":"ঈ",
    "D":"উ",
    "E":"ঊ",
    "F":"ঋ",
    "G":"এ",
    "H":"ঐ",
    "I":"ও",
    "J":"ঔ",

    // <CONSONANTS>
    "K":"ক",
    "L":"খ",
    "M":"গ",
    "N":"ঘ",
    "O":"ঙ",
    "P":"চ",
    "Q":"ছ",
    "R":"জ",
    "S":"ঝ",
    "T":"ঞ",
    "U":"ট",
    "V":"ঠ",
    "W":"ড",
    "X":"ঢ",
    "Y":"ণ",
    "Z":"ত",
    "_":"থ",
    "`":"দ",
    "a":"ধ",
    "b":"ন",
    "c":"প",
    "d":"ফ",
    "e":"ব",
    "f":"ভ",
    "g":"ম",
    "h":"য",
    "i":"র",
    "j":"ল",
    "k":"শ",
    "l":"ষ",
    "m":"স",
    "n":"হ",
    "o":"ড়",
    "p":"ঢ়",
    "q":"য়",
    "r":"ৎ",

    // <DIGITS>
    "0":"০",
    "1":"১",
    "2":"২",
    "3":"৩",
    "4":"৪",
    "5":"৫",
    "6":"৬",
    "7":"৭",
    "8":"৮",
    "9":"৯",

    // Kars
    "v":"া",
    "w":"ি",
    "x":"ী",
    "y":"ু",
    "z":"ু",
    "~":"ূ",
    "„":"ৃ",
    "‡":"ে",
    "†":"ে",
    "‰":"ৈ",
    "ˆ":"ৈ",
     "Š":"ৗ",

    // signs
    "Ô":"‘",
    "Õ":"’",
    "\\|":"।",
    "Ò":"“",
    "Ó":"”",
     
     // Complex
    "s":"ং",
    "t":"ঃ",
    "u":"ঁ",
    "ª":"্র",
    "Ö":"্র",
    "«":"্র",
    "¨":"্য",
    "\\&":"্",
    "…":"ৃ"
}; // end bijoy_string_conversion_map

function ReArrangeUnicodeConvertedText(str)
{
    for (var i=0; i<str.length; i++)
    {
        // for 'Vowel + HALANT + Consonant'
        // it should be 'HALANT + Consonant + Vowel'
        if (i > 0 && str.charAt(i) == '\u09CD' && (IsBanglaKar(str.charAt(i - 1)) || IsBanglaNukta(str.charAt(i - 1))) && i < str.length-1)
        {
            var temp = str.substring(0, i-1);
            temp += str.charAt(i);
            temp += str.charAt(i + 1);
            temp += str.charAt(i - 1);
            temp += str.substring(i + 2, str.length);
            str = temp;
        }

        // for 'RA (\u09B0) + HALANT + Vowel'
        // it should be 'Vowel + RA (\u09B0) + HALANT'
        if (i > 0 && i < str.length - 1 && str.charAt(i) == '\u09CD' && str.charAt(i-1) == '\u09B0'
            && str.charAt(i-2) != '\u09CD' && IsBanglaKar(str.charAt(i + 1)))
        {
            var temp = str.substring(0, i-1);
            temp += str.charAt(i + 1);
            temp += str.charAt(i - 1);
            temp += str.charAt(i);
            temp += str.substring(i + 2, str.length);
            str = temp;
        }

        // Change refs
        if (i < str.length - 1 && str.charAt(i)=='র' && IsBanglaHalant(str.charAt(i+1)) && !IsBanglaHalant(str.charAt(i-1))  )
        {
            var j = 1;
            while(true)
            {
                if(i-j<0)
                    break;
                if(IsBanglaBanjonborno(str.charAt(i-j)) && IsBanglaHalant(str.charAt(i-j-1)))
                    j += 2;
                else if(j==1 && IsBanglaKar(str.charAt(i-j)))
                    j++;
                else
                    break;
            }
            var temp = str.substring(0, i-j);
            temp += str.charAt(i);
            temp += str.charAt(i+1);
            temp += str.substring(i-j, i);
            temp += str.substring(i+2, str.length);
            str = temp;
            i += 1;
            continue;
        }

    // Change pre-kar to post format suitable for unicode
        if (i < str.length - 1 && IsBanglaPreKar(str.charAt(i)) && IsSpace(str.charAt(i+1))==false)
        {
            var temp = str.substring(0, i);
            var j = 1;

            while(IsBanglaBanjonborno(str.charAt(i+j)))
            {
                if(IsBanglaHalant(str.charAt(i+j+1)))
                    j += 2;
                else
                    break;
            }
            temp += str.substring(i+1,i+j+1);

            var l = 0;
            if(str.charAt(i)=='ে' && str.charAt(i+j+1) == 'া')
                { temp += "ো"; l = 1;}
            else if(str.charAt(i)=='ে' && str.charAt(i+j+1) == "ৗ")
                { temp += "ৌ"; l = 1;}
            else
                temp += str.charAt(i);
            temp += str.substring(i+j+l+1, str.length);
            str = temp;
            i += j;
        }

    // nukta should be placed after kars
    // if(i<str.length-1 && IsBanglaNukta(str.charAt(i)) && IsBanglaPostKar(str.charAt(i+1)))
    if(i<str.length-1 && str.charAt(i)=='ঁ' && IsBanglaPostKar(str.charAt(i+1)))
    {
            var temp = str.substring(0, i);
        temp += str.charAt(i+1);
            temp += str.charAt(i);
            temp += str.substring(i+2,str.length);
            str = temp;
    }
    }

    return str;
}

function ConvertToUnicode(ConvertFrom, line)
{
    var conversion_map = bijoy_string_conversion_map;
    if(ConvertFrom=="bijoy")
        conversion_map = bijoy_string_conversion_map;
    
    for (var ascii in conversion_map)
    {
        var myRegExp = new RegExp(ascii, "g");
        line = line.replace(myRegExp, conversion_map[ascii]);
    }
    
    line = ReArrangeUnicodeConvertedText (line);

    var myRegExp = new RegExp("অা", "g");
    line = line.replace(myRegExp, "আ");
        
    return line;
} // end function ConvertBijoyToUnicode