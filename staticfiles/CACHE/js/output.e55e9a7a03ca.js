$('form#CreateSimilarAlert').ajaxForm({type:'POST',dataType:'json',data:$('#CreateSimilarAlert').serialize(),url:' "my:job_alert" %}',success:function(data){console.log(data.error,data.message)
if(data.error==false){$("#create_similarjob_alert").modal('hide')
open_dialog('Success, We will reach you with Profiles of this type','Success!')}
else{$('p.hint').remove();for(var key in data.message){$('#alert_'+key).after('<p class="hint">'+data.message[key]+'</p>');}}}})
$('#similar_job_alert').click(function(){$('p.hint').remove();$('#CreateSimilarAlert')[0].reset()
$("#create_similarjob_alert").modal('show')})
$('#recommended_jobs_carousel').carousel({interval:7000});$('#recommended_jobs_carousel2').carousel({interval:7000});$('body').on('click','.recommended_job',function(){window.location=$(this).find("a").attr("href");});$('.less').click(function(e){e.preventDefault();$(this).addClass('limited_job_posts');$('.see_more').removeClass('limited_job_posts');$(this).siblings('ul').children('li').slice('5').addClass('limited_job_posts');});;$("#multiple").select2({placeholder:"Select a programming language",allowClear:true});$(".redirect_job_click").click(function(e){e.preventDefault()
window.open($(this).find('.job_url').attr('href'))})
$(".redirect_job_click a").click(function(e){e.stopPropagation()})});