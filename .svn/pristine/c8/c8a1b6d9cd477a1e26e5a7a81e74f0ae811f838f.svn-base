/**
 * 
 * @file
 */
jQuery(function($) {

    'use strict';

    $(window).resize(function(){
        // reset_search_result_panel();
    });

    $("#search_result_panel").ready(function(){
        // reset_search_result_panel();
    });

    $('#panel_yang').styleListener({
        styles: ['display'],
        changed: function(style, newValue, oldValue, element) {
            // reset_search_result_panel();
        }
    });

    function reset_search_result_panel(){
        var NORMAL_SCREEN_WIDTH = 1366,
            CONTENT_LEFT_WIDTH = 700,
            $search_result_panel = $("#search_result_panel"),
            $srp_content_left = $("#search_result_panel .content_left");

        if($search_result_panel.width() < CONTENT_LEFT_WIDTH){
            $srp_content_left.css("padding-left", 0);
            $srp_content_left.width($search_result_panel.innerWidth());
        } else if($search_result_panel.width() < NORMAL_SCREEN_WIDTH) {
            $srp_content_left.css("padding-left", $search_result_panel.innerWidth()*0.06);
            $srp_content_left.width($search_result_panel.innerWidth()*(
                    0.48 + (NORMAL_SCREEN_WIDTH-$search_result_panel.width())/NORMAL_SCREEN_WIDTH
                )
            );
        } else {
            $srp_content_left.css("padding-left", $search_result_panel.innerWidth()*0.06);
            $srp_content_left.width($search_result_panel.innerWidth()*0.48);
        }
    }

});