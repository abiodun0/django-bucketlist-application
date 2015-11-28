$(document).ready(function() {
    $('.edit-bucketitem').click(function(e) {
        $(this).closest('.bucket-item').find('form').toggle();
        $(this).closest('.bucket-item').find('.bucket-item-content').toggle();
    })
    $('.bucket-link').hover(function(e) {

        $(this).tooltip('show');

    }).click(function(e) {
        e.preventDefault();
        var bucketlist_name = $(this).closest('.panel').find('.panel-heading').text();
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
