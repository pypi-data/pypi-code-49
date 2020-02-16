JSONViewer = """
function formatJson (msg) {
var rep = '~';
var jsonStr = JSON.stringify(msg, null, rep)
//var matcher = jsonStr.match(/\[(\s|\w-_|'|"|,)*\]/g)
//console.debug(matcher instanceof Array,matcher)
//if(matcher && matcher instanceof Array){
//   for(let m_index = 0;m_index<matcher.length;m_index++){
//       jsonStr.replace(matcher[m_index],matcher.replace(/[\s~]*/g,''))
//   }
//}
var str = '';
for (var i = 0; i < jsonStr.length; i++) {
var text2 = jsonStr.charAt(i)
if (i > 1) {
var text = jsonStr.charAt(i - 1)
if (rep != text && rep == text2) {
//str += '<br/>'
}
}
str += text2;
}
jsonStr = '';
for (var i = 0; i < str.length; i++) {
var text = str.charAt(i);
if (rep == text) { jsonStr += '&nbsp;&nbsp;&nbsp;&nbsp;' } else {
jsonStr += text;
}
if (i == str.length - 2) { jsonStr += '' }
}
return jsonStr.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\\b(true|false|null)\\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function(match) {
                    var cls = 'number';
                    if (/^(&nbsp;)*"/.test(match)) {
                        if (/:$/.test(match)) {
                            cls = 'key';
                        } else {
                            cls = 'string';
                        }
                    } else if (/true|false/.test(match)) {
                        cls = 'boolean';
                    } else if (/null/.test(match)) {
                        cls = 'null';
                    }
                    return '<span class="' + cls + '">' + match + '</span>';
                });
}
"""