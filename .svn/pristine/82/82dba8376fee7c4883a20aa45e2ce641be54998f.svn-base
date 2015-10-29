$(document).ready(function() {

    $(window).resize(function(){
        autoUpdateNavItem();
    });

    $("#nav").ready(function(){
        autoUpdateNavItem();
    });
    $('#panel_yang').styleListener({
        styles: ['display'],
        changed: function(style, newValue, oldValue, element) {
            if( $('#panel_yang').css('display') != 'none' ){
                autoUpdateNavItem();
                $("#search .search_text").focus();
            }
        }
    });
//===================================================================
    function updateNavLogo(){
        if($("#nav ul").width() < 900){
            $("#nav .logo_name").html('C');
            $("#nav .logo_rear").html('Z');
        } else {
            $("#nav .logo_name").html('cz Lib');
            $("#nav .logo_rear").html('');
        }
    } // end function updateNavLogo()

    function autoUpdateNavItem(){
        var NAV_HEIGHT = 40;
        var DELTA = 5;
        // updateNavLogo();
        // alert($("#nav").width() + ';' +$("#nav ul").width() + '; ' + $("#nav_logo").width());
        if($("#nav").height() > NAV_HEIGHT){
            $('#nav #nav_special').removeClass('csshide');
            var li_width_sum = 0;
            $('#nav ul li').each(function(index) {
                if($(this).css('display') != 'none'){
                    li_width_sum += $(this).outerWidth(true);
                }
            });

            for (var i = $('#nav ul li').length-1; i >=0; i--) {
                var this_li = $('#nav ul li').eq(i);
                
                if(this_li.attr('id') != 'nav_logo'  && this_li.attr('id') != 'nav_special'  && this_li.css('display') != 'none'){
                    li_width_sum -= this_li.outerWidth(true);
                    this_li.addClass('csshide');
                    //alert('hide:' + this_li.text());
                    if(li_width_sum + $("#nav #admin").outerWidth(true) + DELTA< $("#nav ul").width()){
                        //alert(this_li.width() + ', ' + this_li.text());
                        if($('#nav ul li').eq(1).css('display') == 'none') { 
                            $("#nav #nav_special a").html('分类'); 
                        }
                        return false; //same with: break;
                    }
                }
            }// end for
        }else{
            //$('#nav #nav_special').addClass('csshide');

            var li_width_sum = 0;
            $('#nav ul li').each(function(index) {
                if($(this).css('display') != 'none'){
                    li_width_sum += $(this).outerWidth(true);
                }
            });

            for (var i = 0; i < $('#nav ul li').length; i++) {
                var this_li = $('#nav ul li').eq(i);
                
                if(this_li.attr('id') != 'nav_logo'  && this_li.attr('id') != 'nav_special'  && this_li.css('display') == 'none'){
                    li_width_sum += this_li.outerWidth(true);
                    if(li_width_sum + $("#nav #admin").outerWidth(true) + DELTA < $("#nav ul").width()){
                        this_li.removeClass('csshide');
                        if($('#nav ul li').eq(1).css('display') != 'none'){  
                            $("#nav #nav_special a").html('&gt;&gt;'); 
                        }
                        if($('#nav ul li').eq($("#nav #nav_special").index()-1).css('display') != 'none'){
                            $("#nav #nav_special").addClass('csshide');
                        }
                    }else{
                        //alert(this_li.width() + ', ' + this_li.text());
                        return false; //same with: break;
                    }
                }
            }// end for
        }
    }// end function

});
