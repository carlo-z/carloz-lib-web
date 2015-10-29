/**
 * 
 * @file
 */
jQuery(function($) {

    'use strict';

    $(window).resize(function(){
        reset_first_pg_search();
    });
    $("#search .search_text").ready(function(){
        reset_first_pg_search();
    });
     $("#search .btn_submit").ready(function(){
        reset_first_pg_search();
    });
    $("#search .search_text").on('focus', function() {
        reset_first_pg_search();
    });
    $("#search .search_form").ready(function(){
        reset_first_pg_search();
    });

//===================================================================
    function reset_first_pg_search(){
        //计算输入框和按钮的宽度、logo字体的大小，适应各种浏览器宽度
        var DELTA = 12, /* $search_text padding-left and padding-right and border*/
            SEARCH_TEXT_LEN = 531,
            screen_width = $(window).width(),
            $search = $("#search"),
            $logo_name = $("#search .logo_name"),
            $logo_rear = $("#search .logo_rear"),
            $search_form = $('#search div.form'),
            $input_keyword = $("#search .search_text"),
            $input_submit = $("#search .btn_submit"),
            $top_nav_bar = $("#nav");

        // 添加竖直方向定位
        var screen_blank =0.2*($(window).height()-$top_nav_bar.height()-$search.height());
        $search.css("margin-top", screen_blank);

        if($search.width() < SEARCH_TEXT_LEN + DELTA){
            $logo_name.css("font-size", 40);
            $logo_rear.css("font-size", 24);
            $input_keyword.width($search.width() - DELTA);
            $search_form.width($input_keyword.outerWidth(true) + 1);
        } else if($search.width() >= SEARCH_TEXT_LEN + DELTA 
                    && $search.width() < SEARCH_TEXT_LEN + DELTA + $input_submit.outerWidth(true) + 1 ) {
            $logo_name.css("font-size", 52);
            $logo_rear.css("font-size", 32);
            $input_keyword.width(SEARCH_TEXT_LEN);
            $search_form.width($input_keyword.outerWidth(true) + 1);
        } else {
            $logo_name.css("font-size", 64);
            $logo_rear.css("font-size", 40);
            $input_keyword.width(SEARCH_TEXT_LEN);
            $search_form.width(
                $input_keyword.outerWidth(true)+ $input_submit.outerWidth(true) + 1
            );
        }
    }// end function

});