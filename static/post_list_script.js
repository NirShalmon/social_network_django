function on_like_unlike(){
    var post_id = $(this).closest('div').attr('id');
    if($(this).text() == 'like'){
        $.post("/like/",
        {
            post_id: post_id,
            csrfmiddlewaretoken: token,
        }
        );
        $(this).text('unlike');
     }else{
        $.post("/unlike/",
        {
            post_id: post_id,
            csrfmiddlewaretoken: token,
        }
        );
        $(this).text('like');
     }
    return false;
}

$(document).ready(function(){
  $(".like_unlike_button").click(on_like_unlike);
});