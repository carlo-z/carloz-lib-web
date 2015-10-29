$(document).ready(function() {

    $('#admin_article #article_list table').ready(function(){   
        //autoAdjustLayout();
        autoAdjustArticleTable();
    });

    $(window).resize(function(){
        //autoAdjustLayout();
        autoAdjustArticleTable();
    });
    function autoAdjustLayout(){
        if($(window).width() > 1024){
            $('#container').addClass('container');
        } else {
            $('#container').removeClass('container');
        }
    }
    function autoAdjustArticleTable(){
        var $article_table = $('#admin_article #article_list table'),
            $container = $('#container'),
            table_width = $article_table.outerWidth(true),
            screen_width = $container.width();
        if (table_width > screen_width){
            for(i=1; i < 6; ++i){
                op_table_column(i, 'hide');
                table_width = $article_table.outerWidth(true),
                screen_width = $container.width();
                if(table_width<=screen_width) break;
            }
        } else {
            for(i=5; i >0; --i){
                op_table_column(i, 'show');
                table_width = $article_table.outerWidth(true),
                screen_width = $container.width();
                if(table_width > screen_width){ 
                    op_table_column(i, 'hide');
                    break;
                }
            }
        }
    }
    function op_table_column(index, op) {
        var op_hide="hide", op_show="show";
        $tr = $('#admin_article #article_list table tr');
        if(op_hide == op) {
            switch(index){
                case 1:
                    $tr.find('th.pv').hide();
                    $tr.find('td.pv').hide();
                    break;
                case 2:
                    $tr.find('th.disuss').hide();
                    $tr.find('td.disuss').hide();
                    break;
                case 3:
                    $tr.find('th.public').hide();
                    $tr.find('td.public').hide();
                    break;
                case 4:
                    $tr.find('th.edit').hide();
                    $tr.find('td.edit').hide();
                    break;
                case 5:
                    $tr.find('th.delete').hide();
                    $tr.find('td.delete').hide();
                    break;
                default: break;
            }
        } else {
            switch(index){
                case 1:
                    $tr.find('th.pv').show();
                    $tr.find('td.pv').show();
                    break;
                case 2:
                    $tr.find('th.disuss').show();
                    $tr.find('td.disuss').show();
                    break;
                case 3:
                    $tr.find('th.public').show();
                    $tr.find('td.public').show();
                    break;
                case 4:
                    $tr.find('th.edit').show();
                    $tr.find('td.edit').show();
                    break;
                case 5:
                    $tr.find('th.delete').show();
                    $tr.find('td.delete').show();
                    break;
                default: break;
            }  
        }
    }
});