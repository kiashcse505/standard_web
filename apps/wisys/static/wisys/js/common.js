
var LIST_ROW_SELECTOR = ".user-checkbox";
var LIST_ROW_SELECTED_CLASS = "row-selected";
var WisysTemplate = function(){}


function confirm_datatable_options(options, datatable) {

    var xeditable_options = {};

    options.fnRowCallback = datatableview.make_xeditable(xeditable_options);
//
    options.sDom = 'C<"clear">irtlp';
    options.oLanguage = {
                            "sLengthMenu": "_MENU_ records per page"
                        };

    options.bAutoWidth = false;
    options.bRetrieve = true;

    return options;
}


jQuery(document).ready(function(){



   var self = $(this);

   WisysTemplate.prototype.setEntityName = function(name){
      self.entityName = name;
   }

   WisysTemplate.prototype.getEntityName = function(){
      return self.entityName;
   }

   WisysTemplate.prototype.registerDefaultModels = function(){

   }

   WisysTemplate.prototype.errorAlert = function(msg, layout ){

       var config = { type:'error' , text: msg , timeout:5000  };
       if( layout != undefined && layout != "" )
            config['layout'] = layout;

       return noty( config );
   }

   WisysTemplate.prototype.successAlert = function(msg, layout ){

       var config = { type:'success' , text: msg, timeout:5000  };
       if( layout != undefined && layout != "" )
            config['layout'] = layout;

       return noty( config );

   }

   WisysTemplate.prototype.confirmAlert = function(msg, layout , callback ){
       $.noty.closeAll();
       var config = { type:'confirm' , text: msg, timeout:5000 , modal: true};
       if( layout != undefined && layout != "" )
            config['layout'] = layout;

       config['buttons'] = [
            {   addClass: 'btn btn-primary', text: 'YES', onClick: callback },
            {   addClass: 'btn btn-danger', text: 'NO', onClick: function($noty) {
                $noty.close();
              }
            }
        ];

       return noty( config );

   }

   WisysTemplate.prototype.infoAlert = function(msg, layout ){

       var config = { type:'information' , text: msg, timeout:5000 };
       if( layout != undefined && layout != "" )
            config['layout'] = layout;

       return noty( config );

   }

   WisysTemplate.prototype.warningAlert = function(msg, layout ){

       var config = { type:'warning' , text: msg, timeout:5000 };
       if( layout != undefined && layout != "" )
            config['layout'] = layout;

       return noty( config );
   }

   WisysTemplate.prototype.registerEntityListingUrl = function( listingUrl ){
        self.listingUrl = listingUrl;
   }

   WisysTemplate.prototype.redirectToEntityListingPage = function(){
       window.location = self.listingUrl;
   }
   WisysTemplate.prototype.registerEntityCRUDUrls = function(createUrl,updateUrl,deleteUrl){
        $("#add-btn").click(function(){
            window.location = createUrl;
        });

        $("#edit-btn").click(function(){
            $.noty.closeAll();
            if (  template.hasSelectedRow() && !template.hasMultipleRowSelected() ){
                template.redirectWithSelectedRow(updateUrl, 99 );
            }else{
                template.errorAlert('Please select a single item.', 'top');
            }

        });

        $('#delete-btn').click(function(){
            $.noty.closeAll();
            if (  template.hasSelectedRow() && !template.hasMultipleRowSelected() ){

                template.confirmAlert('Please confirm this action.', 'top',function(){
                    template.redirectWithSelectedRow(deleteUrl, 99 );
                });

            }else{

                template.errorAlert('Please select a single item.', 'top');

            }
        });


   }


   WisysTemplate.prototype.enableEntityTableListSingleRowSelection = function(callback){

       var oTable = $(".datatable");
       oTable.click( function(event){

           $(oTable).find(LIST_ROW_SELECTOR).prop( "checked" , "" );
           $(oTable).find('tr').removeClass(LIST_ROW_SELECTED_CLASS);

            $(event.target.parentNode).find(LIST_ROW_SELECTOR).prop("checked", "checked");
            $(event.target.parentNode).addClass(LIST_ROW_SELECTED_CLASS);

            if( callback != undefined )
                callback.call(document.body);

       });

    }


    WisysTemplate.prototype.getDataTableObject = function(){
        return $(".datatable").dataTable();
    }

    WisysTemplate.prototype.refreshDataTable = function(){
        var oTable = template.getDataTableObject();
        oTable.fnDraw(false);
    }

    WisysTemplate.prototype.isDataTableInLastPage = function(){
        return ( ( template.getDataTableObject().fnPagingInfo().iTotalPages - 1) ==  template.getDataTableObject().fnPagingInfo().iPage  );
    }

    WisysTemplate.prototype.isDataTableInFirstPage = function(){
        return ( 0 ==  template.getDataTableObject().fnPagingInfo().iPage  );
    }

   //First Row

   WisysTemplate.prototype.getFirstRowSelector = function(){
      return $( LIST_ROW_SELECTOR).first();
   }

   WisysTemplate.prototype.getFirstRowObject = function(){
      return $( LIST_ROW_SELECTOR).first().parents('tr');
   }

   //Last Row

   WisysTemplate.prototype.getLastRowSelector = function(){
      return $( LIST_ROW_SELECTOR).last();
   }

   WisysTemplate.prototype.getLastRowObject = function(){
      return $( LIST_ROW_SELECTOR).last().parents('tr');
   }

   //Selected Row

   WisysTemplate.prototype.getSelectedRowSelectorObject = function(){
      return $( LIST_ROW_SELECTOR + ":checked");
   }

   WisysTemplate.prototype.getSelectedRowObject = function(){
      return template.getSelectedRowSelectorObject().parents('tr');
   }

   WisysTemplate.prototype.getSelectedRowItemId = function(){
       return template.getSelectedRowSelectorObject().val();
   }

   //Selected Prev Row

   WisysTemplate.prototype.getSelectedRowPreviousSelectorObject = function(){
      return template.getSelectedRowPreviousRowObject().find(LIST_ROW_SELECTOR);
   }

   WisysTemplate.prototype.getSelectedRowPreviousRowObject = function(){
      return $( LIST_ROW_SELECTOR + ":checked").parents('tr').prev()
   }

   WisysTemplate.prototype.getSelectedRowPreviousItemId = function(){
       return template.getSelectedRowPreviousSelectorObject().val();
   }

   WisysTemplate.prototype.unselectSelectedRow = function(){

       var selectedRowSelector = template.getSelectedRowSelectorObject();
       var selectedRow = template.getSelectedRowObject();
       selectedRow.removeClass(LIST_ROW_SELECTED_CLASS);
       selectedRowSelector.prop('checked', false);

   }

   WisysTemplate.prototype.selectPreviousRowAndGetItemId = function(){

       var oTable = template.getDataTableObject();

       var itemId = template.getSelectedRowPreviousItemId();

       if( oTable.fnPagingInfo().iTotalPages )

       if( itemId === undefined ) {

           if( template.isDataTableInFirstPage() ) return 0;

           oTable.fnSettings().aoDrawCallback.push({
                "fn": function () {
                    template.getLastRowObject().addClass(LIST_ROW_SELECTED_CLASS);
                    template.getLastRowSelector().prop('checked', true);
                    oTable.fnSettings().aoDrawCallback.pop();
                },
                "sName": "rowSelectionHook"
           });
//           template.unselectSelectedRow();
           template.getDataTableObject().fnPageChange( 'previous' );

           itemId = template.getSelectedRowItemId();

       }else{

           var selectedRowSelector = template.getSelectedRowSelectorObject();
           var selectedRow = template.getSelectedRowObject();
           var previousRow = template.getSelectedRowPreviousRowObject();
           var previousRowSelector = template.getSelectedRowPreviousSelectorObject();

           previousRow.addClass(LIST_ROW_SELECTED_CLASS);
           selectedRow.removeClass(LIST_ROW_SELECTED_CLASS);

           selectedRowSelector.prop('checked', false);
           previousRowSelector.prop('checked', true);
       }

       return itemId;
   }

   WisysTemplate.prototype.selectNextRowAndGetItemId = function(){

       var oTable = template.getDataTableObject();

       var itemId = template.getSelectedRowNextItemId();

       if( itemId == undefined ){

           if( template.isDataTableInLastPage() ) return 0;

           oTable.fnSettings().aoDrawCallback.push({
                "fn": function () {
                    template.getFirstRowObject().addClass(LIST_ROW_SELECTED_CLASS);
                    template.getFirstRowSelector().prop('checked', true);
                    oTable.fnSettings().aoDrawCallback.pop();
                },
                "sName": "rowSelectionHook"
           });

//           template.unselectSelectedRow();
           template.getDataTableObject().fnPageChange( 'next' );
           itemId = template.getSelectedRowItemId();


       }else{

           var selectedRowSelector = template.getSelectedRowSelectorObject();
           var selectedRow = template.getSelectedRowObject();
           var nextRow = template.getSelectedRowNextRowObject();
           var nextRowSelector = template.getSelectedRowNextSelectorObject();

           nextRow.addClass(LIST_ROW_SELECTED_CLASS);
           selectedRow.removeClass(LIST_ROW_SELECTED_CLASS);

           selectedRowSelector.prop('checked', false);
           nextRowSelector.prop('checked', true);
       }

       return itemId;
   }

   //Selected Next Row

   WisysTemplate.prototype.getSelectedRowNextSelectorObject = function(){
      return template.getSelectedRowNextRowObject().find(LIST_ROW_SELECTOR);
   }

   WisysTemplate.prototype.getSelectedRowNextRowObject = function(){
      return $( LIST_ROW_SELECTOR + ":checked").parents('tr').next()
   }

   WisysTemplate.prototype.getSelectedRowNextItemId = function(){
       return template.getSelectedRowNextSelectorObject().val();
   }


   WisysTemplate.prototype.postToUrlWithData = function(url,data){

       if(typeof(data)==='undefined') data = [];

       jQuery.ajax({
            url:   url,
            data:  data,
            method: "post",
            async:false

       });
   }

    WisysTemplate.prototype.hasSelectedRow = function(){
        return $( LIST_ROW_SELECTOR + ":checked").length > 0 ;
    }

    WisysTemplate.prototype.hasMultipleRowSelected = function(){
        return $( LIST_ROW_SELECTOR + ":checked").length > 1 ;
    }

    WisysTemplate.prototype.getRedirectUrl = function( url, key ){
        var itemId = template.getSelectedRowItemId();
        var url = url.replace( key, itemId );
        return url;
    }

    WisysTemplate.prototype.redirectWithSelectedRow = function( url, key ){

       var itemId = template.getSelectedRowItemId();
       template.redirectWithItemId(url, key, itemId);

    }

    WisysTemplate.prototype.checkAndRedirectWithSelectedRow = function( url, key ){
        $.noty.closeAll();

        if ( !template.hasSelectedRow() ){
            template.errorAlert('Please select an item first.', 'top');
        }else if (  template.hasSelectedRow() && !template.hasMultipleRowSelected() ){
                template.redirectWithSelectedRow(url, key );
        }else{
            template.errorAlert('Please select a single item.', 'top');
        }
    }

    WisysTemplate.prototype.checkAndRedirectWithSelectedRowWithCustomText = function( url, key, text ){
        $.noty.closeAll();

        if ( !template.hasSelectedRow() ){
            template.errorAlert(text, 'top');
        }else if (  template.hasSelectedRow() && !template.hasMultipleRowSelected() ){
                template.redirectWithSelectedRow(url, key );
        }else{
            template.errorAlert('Please select a single item.', 'top');
        }
    }


    WisysTemplate.prototype.redirectWithItemId = function( url, key, itemId ){
       var url = url.replace( key, itemId );
       window.location = url;
    }

    WisysTemplate.prototype.initIntervalDateTimePicker = function( startSelector, endSelector ){

        if( startSelector == undefined || startSelector == "" )
            startSelector = ".start-date-datetimepicker";

        if( endSelector == undefined || endSelector == "" )
            endSelector = ".end-date-datetimepicker";

        var now = new Date();
        var startSelectorInput = $(startSelector).datetimepicker({
                language: 'en-US',
                startDate: now
        });

        var endSelectorInput = $(endSelector).datetimepicker({
             language: 'en-US',
             startDate: now
        });

        $(startSelector).datetimepicker().on('changeDate', function(ev){
            $(endSelector).datetimepicker('setStartDate', ev.date);
            $(endSelector).datetimepicker('setDate', ev.date);
        });


    }

    WisysTemplate.prototype.previewSelectedImage = function(inputListener, targetToShow){

        var reader = new FileReader(),
            i=0,
            numFiles = 0,
            imageFiles;

        // use the FileReader to read image i
        function readFile() {
            reader.readAsDataURL(imageFiles[i])
        }

        // define function to be run when the File
        // reader has finished reading the file
        reader.onloadend = function(e) {

            // make an image and append it to the div
            var image = $('<img>').attr('src', e.target.result);
            $(image).appendTo(targetToShow);

            // if there are more files run the file reader again
            if (i < numFiles) {
                i++;
                readFile();
            }
        };

        $(inputListener).change(function() {

            imageFiles = document.getElementById('files').files
            // get the number of files
            numFiles = imageFiles.length;
            readFile();

        });
    }

   template = new WisysTemplate();
//    template.enableEntityTableListSingleRowSelection();

//    $('.date').datetimepicker({ pickTime: false });

});


