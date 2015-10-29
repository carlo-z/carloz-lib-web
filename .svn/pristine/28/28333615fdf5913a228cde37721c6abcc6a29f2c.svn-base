/**
 *
 * @file
 */
jQuery(function($) {

    'use strict';

    $(".write-blog").ready(function(){
        $(".write-blog #editor_code").parent().css("display", "none");
        $(".write-blog #tag_list").parent().css("display", "none");
        $(".write-blog #access_pw").parent().removeClass("form-group");
        $(".write-blog #access_pw").parent().addClass("by-password-div");
    });

    $(document).ready(function(){

        setInterval(save_draft, 600000);  // save_draft_task, 10 min once

        var $article_form = $(".write-blog form"),
            $article_form_submit = $("#release_article"),
            $article_form_save = $("#save_draft"),
            $save_draft_state = $("#save_draft_state");

        $article_form_submit.click(function(){
            $article_form.submit();
        });
        $article_form_save.click(function(){
            save_draft();
        });

        function save_draft(){
            var options = {
                url: $article_form.attr('action') + '&option=save_draft',
    　　　　　　  type:'post',
                dataType:'json',
    　　　　　　  success:function(data){
                    $article_form.attr('action', data.form_url);
                    $save_draft_state.text("save draft success");
                    setTimeout(function(){$save_draft_state.text("");}, 10000);
                }
            };
            $article_form.ajaxSubmit(options);
            return false; //stop page jump
        }
    });
});