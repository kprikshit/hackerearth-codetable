// File name related functions
function showFileRename(){
    $(".filename-text").show();
    $("#file-name").hide();
}

function saveFileName(){
    var nname =$("#file-name-value").val();
    if(nname == ""){
        nname= "Untitled File";
    }
    $("#file-name").html(nname);
    hideFileRename();
}

function hideFileRename(){
    $(".filename-text").hide();
    $("#file-name").show();
}

// custom test Input related function
function showInputTextArea(){
    var checked = $('#test-input-checkbox').is(":checked");
    if(checked){
        $(".test-input-container").show();
    }
    else{
        $(".test-input-container").hide();
    }
}

function textInputSpanClick(){
    var checked = $('#test-input-checkbox').is(":checked");
    if(checked){
        $(".test-input-container").hide();
        $('#test-input-checkbox').prop('checked', false);
    }
    else{
        $(".test-input-container").show();
        $('#test-input-checkbox').prop('checked', true);
    }
}


// this function changes the mode of ACE editor when user changes the langauge
// this will also fetch a new template from the server
function changeMode(new_lang, fetchCode){
    var editor = ace.edit("editor");

    if(new_lang == "C")
        editor.session.setMode("ace/mode/c_cpp");
    else if(new_lang == "CPP")
        editor.session.setMode("ace/mode/c_cpp");
    else if(new_lang == "CPP11")
        editor.session.setMode("ace/mode/c_cpp");
    else if(new_lang == "JAVA")
        editor.session.setMode("ace/mode/java");
    else if(new_lang == "JAVASCRIPT")
        editor.session.setMode("ace/mode/javascript");
    else if(new_lang == "PERL")
        editor.session.setMode("ace/mode/perl");
    else if(new_lang == "PYTHON")
        editor.session.setMode("ace/mode/python");
    else if(new_lang == "PHP")
        editor.session.setMode("ace/mode/php");
    else if(new_lang == "RUBY")
        editor.session.setMode("ace/mode/ruby");
    else
        editor.session.setMode("ace/mode/text");
    // fetch a new starter code from server
    if(fetchCode){
        fetch_default_code(new_lang);
    }
}