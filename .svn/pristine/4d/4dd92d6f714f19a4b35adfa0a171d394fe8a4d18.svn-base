/**
 * 
 * @file
 */
jQuery(function($) {

    'use strict';

    $(window).resize(function(){
        resetGlobalSearch();
    });
    $(".g_search_bar form").ready(function(){
        resetGlobalSearch();
    });
    $('#panel_yin').styleListener({
        styles: ['display'],
        changed: function(style, newValue, oldValue, element) {
            if( $('#panel_yin').css('display') != 'none' ){
                resetGlobalSearch();
            }
        }
    });
    $("#panel_yin .g_search_bar .search_text").on('focus', function() {
        resetGlobalSearch();
    });

//===================================================================
    function resetGlobalSearch(){
        //计算输入框和按钮的宽度、logo字体的大小，适应各种浏览器宽度
        var DELTA = 12, /* $search_text padding-left and padding-right and border*/
            SEARCH_TEXT_LEN = 500,
            $g_search_bar = $('#panel_yin').css('display') != 'none' ? 
                            $("#panel_yin .g_search_bar") : 
                            $("#panel_yang .g_search_bar"),
            $logo =  $('#panel_yin').css('display') != 'none' ? 
                            $("panel_yin .g_search_bar .logo") : 
                            $("panel_yang .g_search_bar .logo"),
            $search_text = $('#panel_yin').css('display') != 'none' ? 
                           $("#panel_yin .g_search_bar .search_text") : 
                           $("#panel_yang .g_search_bar .search_text");

        if($g_search_bar.width() - $logo.outerWidth(true)-1 < SEARCH_TEXT_LEN + DELTA) {
            $search_text.width($g_search_bar.width()-DELTA);
        } else {
            $search_text.width(SEARCH_TEXT_LEN);
        }
    }// end function

});