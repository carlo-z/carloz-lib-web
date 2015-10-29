/**
 * 
 * @file
 */
jQuery(function($) {

    'use strict';

    var PANEL_OPEN_STATE = false, //panle open state
        isInput = false,
        $panel_yang = $("#panel_yang"),
        $panel_yin = $("#panel_yin"),
        $searchInput = $("#panel_yin .g_search_bar .search_text"),
        $elevator = $("#elevator");

    $searchInput.on("close", function() {
        hidePanel();
    }).on('focus', function() {
        isInput = true;
        $(this).addClass("focus");
    }).on('blur', function() {
        isInput = false;
        $(this).removeClass("focus");
    });

    $(document).on("keydown", function(evt) {
        if(isInput) { return; }
        if(evt.ctrlKey && evt.keyCode === 81) {//ctrl + q
           $(document).trigger('togglepanel');
        } else if(evt.keyCode === 27) {//esc close
            hidePanel();
        }
    }).on("click", function() {
        //complete.hide();
    }).on("togglepanel", function() {
        !PANEL_OPEN_STATE ? showPanel() : hidePanel();
    });

    $(".search-tip-btn").on("click", function() {
        $(this).attr("data-type") === 'open' ? showPanel() : hidePanel();
        return false;
    });

    //Elevator
    $(document).on("scroll", function() {
        var scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
        if(scrollTop > 0) {
            $elevator.fadeIn();
        } else {
            $elevator.fadeOut();
        }
    });

    function hidePanel() {
        PANEL_OPEN_STATE = false;
        document.documentElement.style.overflow = '';
        document.body.style.overflow = '';
        $panel_yang.show();
        $panel_yin.hide();
        $searchInput.blur();
    }

    function showPanel() {
        PANEL_OPEN_STATE = true;
        document.documentElement.style.overflow = '';
        document.body.style.overflow = '';
        $panel_yang.hide();
        $panel_yin.show();
        $searchInput.focus();
    }
});