/**
 *
 * @file
 */
jQuery(function($) {

    'use strict';


    $("#article_body").ready(function(){
        $("img.lazy").lazyload({effect : "fadeIn"});
        set_img_max_width();
    });

    function set_img_max_width() {
        var $article_body = $('#article_body'),
            $img_list_in_article = $('#article_body img');

        $img_list_in_article.each(function() {
            var maxWidth = $article_body.innerWidth(); // 图片最大宽度
            $(this).css('max-width', maxWidth); // 设定实际显示宽度

            $(this).removeAttr('width');
            $(this).removeAttr('height');
        });
    }

    function adjust_img_size(){
        var $article_body = $('#article_body'),
            $img_list_in_article = $('#article_body img');

        $img_list_in_article.each(function() {
            var maxWidth = $article_body.innerWidth(); // 图片最大宽度
            var maxHeight = $article_body.innerHeight();    // 图片最大高度
            var ratio = 0;  // 缩放比例
            var width = $(this).width();    // 图片实际宽度
            var height = $(this).height();  // 图片实际高度

            // 检查图片是否超宽
            if(width > maxWidth){
                ratio = maxWidth / width;   // 计算缩放比例
                $(this).css("width", maxWidth); // 设定实际显示宽度
                height = height * ratio;    // 计算等比例缩放后的高度
                $(this).css("height", height);  // 设定等比例缩放后的高度
            }

            // 检查图片是否超高
            if(height > maxHeight){
                ratio = maxHeight / height; // 计算缩放比例
                $(this).css("height", maxHeight);   // 设定实际显示高度
                width = width * ratio;    // 计算等比例缩放后的高度
                $(this).css("width", width * ratio);    // 设定等比例缩放后的高度
            }
        });
    } // end function adjust_img_size

});