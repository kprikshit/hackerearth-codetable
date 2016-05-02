function saveCode(code_id){
            $("#save-code").text("Saving...");
            var editor = ace.edit("editor");
            var code_text = editor.session.getValue();
            var code_lang = $("#lang").val();
            $.post({
                type :'POST',
                url: '/editor/save/',
                data: {'lang': code_lang, 'text': code_text, 'id': code_id},
                success: function(response){
                    $(".date-last-saved-value").html(new Date(response));
                    $("#save-code").text("Saved!");
                    $("#save-code").css("background-color", "green");
                },
                error: function(error){
                    console.log(error);
                }
            })
        }

        // this will save the code first and then it will run it
        function saveCompileRun(code_id) {
            while (1) {
                saveCode(code_id);
                break;
            }
            compileAndRun(code_id);
        }

        function compileAndRun(code_id){
            $("#output").hide();
            $("#error").hide();
            $("#compiling").show();

            var code_input = $("#test-input").val();
            $.ajax({
                method: 'POST',
                url: '/editor/run/',
                dataType: 'json',
                data: {'id': code_id, 'input': code_input},
                success: function(runData){
                    $("#compiling").hide();
                    if(runData.error == 0) {
                        $("#output").show();
                        $("#output-compile-status").html(runData.compile_status);
                        $("#output-input-value").html(runData.input);
                        $("#output-output-value").html(runData.output);
                        $("#output-memory-used-value").html(runData.memory_used);
                        $("#output-time-used-value").html(runData.time_used);
                        $("#output-status-value").html(runData.status);
                        $("#output-status-detail-value").html(runData.status_detail);
                    }
                    else{
                        $("#error").show();
                        $("#error-status").html(runData.compile_status);
                    }
                },
                error: function(error){
                    $("#compiling-holder").hide();
                }
             });
        }

        function deleteCode(code_id){

        }

        function share(code_id){
            $.ajax({
                type: 'POST',
                data: {'code_id': code_id},
                url: '/editor/generate/',
                success: function(response){
                    $("a#share-url-href").attr("href", response);
                    $("a#share-url-href").text(response);
                    $("#share-url-href").show();
                },
                error: function(error){
                    $("a#share-url-href").text(response);
                    $("#share-url-href").show();
                }
             })
        }

        function fetch_default_code(new_lang){
            var editor = ace.edit("editor");
            var code_id = $("#codeiddiv").html();
            $.post({
                type :'POST',
                url: '/editor/starter/',
                data: {'lang': new_lang},
                success: function(response){
                    editor.session.setValue(response);
                },
                error: function(error){
                    console.log(error);
                }
            })
        }