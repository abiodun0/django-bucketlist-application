$(document).ready(function() {
    alertTimeout = setTimeout(function(){
        $(".alert").remove();
    },3000);
    if($.isEmptyObject($.find('.alert'))) clearTimeout(alertTimeout);
    $('.edit-bucketitem').click(function(e) {
        $(this).closest('.bucket-item').find('form').toggle();
        $(this).closest('.bucket-item').find('.bucket-item-content').toggle();
    })
    $(".new-bucket-link").hover(function(e){
        $(this).tooltip('show');
    });
     $('.done').on('change',function(){
        console.log("check");
        $(this).closest("form").trigger("submit");
    });
    $('.bucket-link').hover(function(e) {

        $(this).tooltip('show');

    }).click(function(e) {
        e.preventDefault();
        var bucketListName = $(this).closest('.page-header').find('h1').text()
        var dashboardBucketListName = $(this).closest('.panel').find('.panel-heading').text();
        var bucketlist_name =  dashboardBucketListName.length > 0 ? dashboardBucketListName: bucketListName;
        $("#itemModal").modal("show");
        var url = $(this).data('action')
        $("#itemModal").find('.modal-title').text("Add new item to " + bucketlist_name);
        $("#itemModal").find('form').attr('action', url);
    });
    $('.delete-bucketitem').click(function(e) {
        e.preventDefault();
        $(this).popover({
            container: false,
            template: '<div class="popover" role="tooltip" style="width:300px;color:black">' +
                '<div class="arrow"></div><h3 class="popover-title"></h3>' +
                '<div class="popover-content"></div></div>',
            html: true,
        });

    });
});
