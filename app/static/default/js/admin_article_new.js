/**
 *
 * @file
 */
jQuery(function($) {

    'use strict';

    $(".write-blog").ready(function(){
        $(".write-blog #editor_code").parent().css("display", "none");
        $(".write-blog #tag_list").parent().css("display", "none");
        /*$(".write-blog #access_pw").parent().css("display", "none");*/
        $(".write-blog #access_pw").parent().removeClass("form-group");
        $(".write-blog #access_pw").parent().addClass("by-password-div");
    });
    $("#release_article").click(function(){
        $(".write-blog form").submit();
    });

});