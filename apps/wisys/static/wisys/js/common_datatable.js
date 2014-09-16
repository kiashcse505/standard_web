var LIST_ROW_SELECTOR = ".user-checkbox";
var JSTemplate = function(){}


jQuery(document).ready(function(){

    JSTemplate.prototype.postToUrlWithData = function(postUrl,postData){
            if(typeof(postData)==='undefined') postData = [];
            $.ajax({
                url : postUrl,
                type : "POST",
                data : postData,
                success :   function(json) {
                                //alert("Delete Successful "+json["patientID"]);
                                var oTable = $('.data-table').dataTable();
                                var row = $(".user-checkbox" + ":checked").closest('tr').get(0);
                                oTable.fnDeleteRow(oTable.fnGetPosition(row))
                                //var iPos= $(rowTable).parent().children().index($(rowTable));
                                //oTable.fnDeleteRow( iPos );
                                $('#confirmModel').modal('show');

                            },
                error :     function(xhr,errmsg,err) {
                                //alert(postData);
                                //alert("Delete Failed");
                                $('#alertModel').modal('show');
                                //alert("Failed "+errmsg+" error "+err+" xhr "+xhr+" postData "+postData);
                            }
            });
    }

    JSTemplate.prototype.enableDatatable = function(ajaxUrl,columnData){
        var oTable = $('.data-table').dataTable({
            "sDom": 'C<"clear">irtlp',
            "bPaginate": true,
            "sPaginationType": "bootstrap",
            "oLanguage": {
                "sLengthMenu": "_MENU_ records per page"
            },
            "bAutoWidth": true,
            "bServerSide": true,
            "sAjaxSource": Django.url(ajaxUrl),
            "fnRowCallback": function( nRow, aData, iDisplayIndex, iDisplayIndexFull ) {
                                  //if ( aData[0] == "checkbox" )
                                  //{
                                      console.log(aData);
                                      $('td:eq(0)', nRow).html( '<input class="user-checkbox" type="checkbox" name="aPatient_id" value="'+aData.id+'">' );
                                  //}
                                  return nRow;
                             },
            "aoColumns": columnData,
            "oTableTools": {
                "sRowSelect": "single"
            }



        });

        return oTable;
    }

    JSTemplate.prototype.fnFilterColumn = function(filterNo,colNo){
        $('.data-table').dataTable().fnFilter(
            $("#filter-"+filterNo).val(),
            colNo
        );
    }

    JSTemplate.prototype.createFilter = function(filterNo,colNo){
        return function() { template.fnFilterColumn(filterNo,colNo); };
    }

    var template = new JSTemplate();
});

