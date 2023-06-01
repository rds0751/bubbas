$(document).ready(function(e){$('.advanced_tag_div').click(function(e){$('#adv_search').plainModal('open');});$('.filter_drop_down .input_filter').focus(function(e){$('.filter_drop_down').css('position','relative')});$('.filter_title').click(function(){if($(this).find('span i').hasClass('fa-chevron-down')){$(this).siblings('.filter_options').slideUp('slow');$(this).children('span').children('i').removeClass('fa-chevron-down').addClass('fa-chevron-up');}
else{$('.fa-chevron-down').parent().parent().next().slideUp('slow');$('.fa-chevron-down').removeClass('fa-chevron-down').addClass('fa-chevron-up');$(this).siblings('.filter_options').slideDown('slow');$(this).children('span').children('i').removeClass('fa-chevron-up').addClass('fa-chevron-down');}});$('li.filter_option').click(function(){if($(this).children('span').hasClass('check_check')){$(this).children('span').removeClass('check_check');$(this).addClass('active');}
else{$(this).children('span').addClass('check_check');$(this).removeClass('active');}});$('form#MailRegisterForm').ajaxForm({type:'POST',dataType:'json',data:$('#MailRegisterForm').serialize(),url:'/registration/using_email/',success:function(data){if(data.error==false){open_dialog("You are successfully Registered, A verification mail has been sent to Your Mail "+(data.user_email),'Success!')
window.location="/user/reg_success/";}
else if(data['password_error']){$('p.hint').remove();$('#mail_password').after('<p class="hint">'+data['password_error']+'</p>');}
else if(data.response){$('p.hint').remove();for(var key in data.response){$('#mail_'+key).after('<p class="hint">'+data.response[key]+'</p>');}}
else{$('p.hint').remove();$('#mail_response_message').text('');$('#mail_response_message').after('<p class="hint">'+data.response_message+'</p>');}}});$('.jobseeker_login').click(function(e){e.preventDefault();$('p.hint').remove();$('#login_register').modal('show');$.post('/jobs/applied_for/',{'job_id':$(this).attr('id')},function(data){},'json')})});$(".filter_icon").click(function(e){e.preventDefault()
if($(this).hasClass('collapsed')){$(this).children().addClass('glyphicon-minus')
$(this).children().removeClass('glyphicon-plus')}
else{$(this).children().removeClass('glyphicon-minus')
$(this).children().addClass('glyphicon-plus')}
return})
$('input, select').keydown(function(){$(this).parent().find('p.hint').remove()});function open_dialog(text,title){var myPos=[$(window).width()/2,50];$('#block_question').text(text);$('#block_question').dialog({modal:true,title:title,draggable:false,position:myPos,buttons:[{text:"OK",click:function(){$(this).dialog("close");$('header').removeClass('fixed')}}]});$('.ui-dialog-titlebar-close').html('<span>X</span>')}
function open_dialog_with_url(text,title,url){var myPos=[$(window).width()/2,50];$('#block_question').text(text);$('#block_question').dialog({modal:true,title:title,draggable:false,position:myPos,buttons:[{text:"OK",click:function(){window.location=url;}}]});$('.ui-dialog-titlebar-close').html('<span>X</span>')}
$('form#ApplicantLoginForm').submit(function(e){e.preventDefault();register_type=$('#register_type').val()
if(register_type=='login'){url='/applicant/login/'}else if(register_type=='forgot_password'){url='/user/forgot_password/'}
else{url='/registration/using_email/'}
$.ajax({type:'POST',dataType:'json',data:$('#ApplicantLoginForm').serialize(),url:url,success:function(data){if(data.error==false){if(register_type=='register'){window.location="/user/reg_success/"}
else if(register_type=='forgot_password'){open_dialog_with_url('Sent a link to your email, reset your password by clicking that link',"Success!",'/')}
else{window.location=data.redirect_url;}}
else if(data.response){$('p.hint').remove();for(var key in data.response){$('#user_login_'+key).after('<p class="hint">'+data.response[key]+'</p>');}}
else{$('p.hint').remove();$('#user_response_message').html('<p class="hint">'+data.response_message+'</p>');}}});});$('form#JobMailRegisterForm').submit(function(e){e.preventDefault();register_type=$('#left_register_type').val()
if(register_type=='login'){url='/applicant/login/'}else if(register_type=='forgot_password'){url='/user/forgot_password/'}
else{url='/registration/using_email/'}
$.ajax({type:'POST',dataType:'json',data:$('#JobMailRegisterForm').serialize(),url:url,success:function(data){if(data.error==false){if(register_type=='forgot_password'){open_dialog_with_url('Password reset Successfull, Check your email for new password',"Success!",'/')}
else{window.location=data.redirect_url;}}
else if(data.response){$('p.hint').remove();for(var key in data.response){$('#mail_'+key).after('<p class="hint">'+data.response[key]+'</p>');}}
else{$('p.hint').remove();$('#mail_response_message').html('<p class="hint">'+data.response_message+'</p>');}}});});$(".login_modal").click(function(e){e.preventDefault()
$("#login_register").modal('show')
$("#login_li").addClass('active')
$("#sign_up_li").removeClass('active')
$("#modal_head").hide()
$("#login_div").show()
$("#register_div").hide()
$('#user_register_type').val('login')
$('p.hint').remove();$('#button_value').text('Login Here')
$('#userlogin_password').show()
$('#pop_up_header').text('Already a Member? Login')
$('#forgot_pass').show()})
$(".sign_up_li").click(function(){$("#login_div").hide()
$("#register_div").show()
$("#modal_head").show()
$('#user_register_type').val('register')
$('p.hint').remove();$()
$('#button_value').text('Register Now')
if(applying_for_job==true){$('form#ApplicantFormRegister .resume_class').hide()
$('form#ApplicantFormRegister .help_text').hide()}})
$("#login_but").click(function(){$("#login_register").modal('show')
$("#login_li").addClass('active')
$('#forgot_pass').show()
$("#modal_head").hide()
$("#login_div").show()
$("#register_div").hide()
$('#user_register_type').val('login')
$('p.hint').remove();$('#button_value').text('Login Here')
$('#userlogin_password').show()
$('#pop_up_header').text('Already a Member? Login')})
$(".sign_in_li").click(function(){$("#login_li").addClass('active')
$("#sign_up_li").removeClass('active')
$("#modal_head").hide()
$('#pop_up_header').text('Already a Member? Login')
$('#user_register_type').val('login')
$('p.hint').remove();$('#button_value').text('Login Here')
$('#userlogin_password').show()
$('#forgot_pass').show()})
$('#forgot_pass_but').click(function(){$('#forgot_pass').hide()
$("#login_div").show()
$("#register_div").hide()
$('#pop_up_header').text('Reset Your Password')
$('#user_register_type').val('forgot_password')
$('#userlogin_password').hide()
$('p.hint').remove();$('#button_value').text('SUBMIT')
$("#modal_head").hide()})
$('#forgot_pass').click(function(){$(this).hide();$("#modal_head").hide()
$("#login_li").removeClass('active')
$("#sign_up_li").removeClass('active')
$('#pop_up_header').text('Reset Your Password')
$('#user_register_type').val('forgot_password')
$('#userlogin_password').hide()
$('p.hint').remove();$('#button_value').text('SUBMIT')})
$('.new_account').click(function(e){e.preventDefault();$('#login_register').modal('show');$("#modal_head").show()
$('p.hint').remove();$('#login_div').hide()
$('#register_div').show()
$('#ApplicantFormRegister').get(0).reset()});$('.new_user_login').click(function(e){e.preventDefault();$('.login_text').text('Already a Member? Login')
$("#modal_head").hide()
$('#register_type').val('login')
$('.new_user_login').hide()
$('.new_account').show()
$('p.hint').remove();$('.login_form_button').text('Sign In')
$('#user_login_password').show()
$('.forgot_password').show()});$('.forgot_password').click(function(e){e.preventDefault();$(this).hide();$("#modal_head").hide()
$('.login_text').text('Reset Your Password')
$('#register_type').val('forgot_password')
$('.new_user_login').show()
$('.new_account').show()
$('#user_login_password').hide()
$('p.hint').remove();$('.login_form_button').text('SUBMIT')});$('.left_new_account').click(function(e){e.preventDefault();$('#login_register').modal('show');$("#modal_head").show()
$("#login_div").hide()
$("#register_div").show()
$('#pop_up_header').text('New User? Register Now')
$('p.hint').remove();$('#button_value').text('Register Now')});$('.left_new_user_login').click(function(e){e.preventDefault();$('.left_login_text').text('Already a Member? Login')
$('#left_register_type').val('login')
$('.left_new_user_login').hide()
$("#modal_head").hide()
$('.left_new_account').show()
$('p.hint').remove();$('.left_login_form_button').text('Sign In')
$('#mail_password').show()
$('.left_forgot_password').show();});$('.left_forgot_password').click(function(e){e.preventDefault();$('.left_forgot_password').hide();$('.left_login_text').text('Reset Your Password')
$('#left_register_type').val('forgot_password')
$('.left_new_user_login').show()
$('.left_new_account').hide()
$('#mail_password').hide()
$("#modal_head").hide()
$('p.hint').remove();$('.left_login_form_button').text('SUBMIT')});$('form#ApplicantForm').submit(function(e){e.preventDefault();register_type=$('#user_register_type').val()
if(register_type=='login'){url='/applicant/login/'}else if(register_type=='forgot_password'){url='/user/forgot_password/'}
else{url='/registration/using_email/'}
$.ajax({type:'POST',dataType:'json',data:$(this).serialize(),url:url,success:function(data){if(data.error==false){if(register_type=='forgot_password'){open_dialog_with_url('Password reset Successfull, Check you email for new password',"Success!",'/')}
else{window.location=data.redirect_url;}}
else if(data.response){$('p.hint').remove();$('p.hint').remove();for(var key in data.response){$('#userlogin_'+key).after('<p class="hint">'+data.response[key]+'</p>');}}
else{$('p.hint').remove();$('#userlogin_response_message').html('<p class="hint">'+data.response_message+'</p>');}}});});$('form#ApplicantFormRegister').submit(function(e){e.preventDefault();$('.register_form_button').prop('disabled',true);$(".register_click").hide()
$(".load_register").show()
var formData=new FormData($(this)[0]);$.ajax({type:'POST',dataType:'json',data:formData,enctype:'multipart/form-data',processData:false,contentType:false,url:'/registration/using_email/',success:function(data){$('.register_form_button').prop('disabled',false);if(data.error==false){if(applying_for_job==true){$("#register_div").hide()
$('#candidate_educationform').show()
$('#modal_head').text('EDUCATION DETAILS')}
else{window.location=data.redirect_url}}
else if(data.response){$(".register_click").show()
$(".load_register").hide()
$('p.hint').remove();for(var key in data.response){if(key=='technical_skills'){$('.reg_skill_err').html('<p class="hint">'+data.response[key]+'</p>');}
else if(key=='current_city'){$('.city_err').html('<p class="hint">'+data.response[key]+'</p>');}
else{$('#user_register_'+key).after('<p class="hint">'+data.response[key]+'</p>');}}}
else{$('p.hint').remove();$('#user_register_response_message').html('<p class="hint">'+data.response_message+'</p>');}}});});function updating_profile_progress_percantage(profile_value){$('#circle').circleProgress({value:profile_value/100,size:100,startAngle:-Math.PI/2,fill:{gradient:[['#0681c4',.5],['#4ac5f8',.5]],gradientAngle:Math.PI/4}});}
$('form#resumeupload').submit(function(){$(".modal_loading").show()
var formData=new FormData($(this)[0]);$.ajax({url:'/upload_resume/',type:'POST',dataType:'json',data:formData,enctype:'multipart/form-data',processData:false,contentType:false,success:function(data){$(".modal_loading").hide()
if(data.error==false){open_dialog_with_url('Resume Uploaded successfully','Success','.')}else{$("#resume").val('')
open_dialog(data.data,'Info!')}}})});$('form#uploadresume').submit(function(e){e.preventDefault()
var formData=new FormData($(this)[0]);$.ajax({url:'/registration/using_email/',type:'POST',dataType:'json',data:formData,enctype:'multipart/form-data',processData:false,contentType:false,success:function(data){$('#get_resume').val('')
$('p.hint').remove();$(".new_account").click()
$('#user_register_email').val(data.resume_email)
$('#user_register_mobile').val(data.resume_mobile)}})});$(".upload_btn_resume").click(function(e){e.preventDefault()
e.stopPropagation()
$('#register_from').val('Resume')
$('#get_resume').click();})
$('#get_resume').change(function(){var clone=$(this).clone();clone.attr('id','user_register_resume');clone.attr('name','resume');$('.resume_class').html(clone);$("#user_register_resume").show()
$("form#uploadresume").submit()});$('#resume_upload_but').click(function(e){e.preventDefault()
$('#resume').click();});$('#resume').change(function(){$("form#resumeupload").submit()});$('#job_skills').on("select2:selecting",function(e){$(".skill_err").hide()
$('p.hint').remove()});$('.walkin_block a').click(function(e){e.stopPropagation()});$(".walkin_block").click(function(e){e.preventDefault()
window.location=$(this).attr('id')})
$('.recruiter_block').click(function(){window.location=$(this).attr('id')})
$('.recruiter_block a').click(function(e){e.stopPropagation()});$('.redirect_link').click(function(){window.location=$(this).attr('data-href')})
$('.add_another').click(function(e){$(this).closest('form').submit();$(this).addClass('save_other')});var applying_for_job=false
var job_id=""
var job_apply_url=""
$('.search-form').submit(function(e){form=$(this)
name=this.name
var skill=form.find('[name="q"]').val().trim();var job_type=$('#job_type').val()
var location=form.find('[name="location"]').val().trim();if((skill==''||skill==null)&(location==''||location==null)){setTimeout(open_dialog('Please select atleast one location or skill','Info!!!'),12000);return false;}
else{$.ajax({url:'/get/search-slugs/',async:false,data:{'q_slug':skill,'location':location},success:function(data){skill_slug=data.skill_slug
location_slug=data.location_slug}})
if(location.length>0&&skill.length==0){if(job_type=='Fresher'){url='/fresher-jobs-in-'+location_slug+'/'}
else if(job_type=='walk-in'){url='/walkins-in-'+location_slug+'/'}
else{url='/jobs-in-'+location_slug+'/'}}
if(skill.length>0&&location.length>0){if(job_type=='Fresher'){url='/'+skill_slug+'-fresher-jobs-in-'+location_slug+'/'}
else if(job_type=='walk-in'){url='/'+skill_slug+'-walkins-in-'+location_slug+'/'}
else{url='/'+skill_slug+'-jobs-in-'+location_slug+'/'}}
if(skill.length>0&&location.length==0){if(job_type=='Fresher'){url='/'+skill_slug+'-fresher-jobs/'}
else if(job_type=='walk-in'){url='/'+skill_slug+'-walkins/'}
else{url='/'+skill_slug+'-jobs/'}}
if(job_type&&job_type!='Fresher'&&job_type!='walk-in'){url+='?job_type='+job_type}
document.forms[name].action=url
return true;}});$(".send_mail").click(function(e){e.preventDefault()
verified=$(this).hasClass('active')
completed=$(this).hasClass('completed')
logged=$(this).hasClass('logged')
if(verified&&completed&&logged){window.location=$(this).attr('href')}
else{if(!logged){$('#login_register').modal('show');}
else if(!verified){open_dialog('You need to verify your Email to apply For this Job','Info!')}
else if(!completed){open_dialog_with_url('Please complete your profile to apply for this job','Info!','/profile/')}}})
$(".customGPlusSignIn").click(function(e){window.location=$(this).attr('data-href')})
$('.job_apply_login').click(function(e){e.preventDefault();applying_for_job=true
job_id=$(this).attr('id')
job_apply_url=$(this).attr('data-href');$('p.hint').remove();$("#login_div").show()
$("#register_div").hide()
$('#login_register').modal('show');$.post('/jobs/applied_for/',{'job_id':$(this).attr('id')},function(data){},'json')})
$('.job_apply_register').click(function(e){e.preventDefault();$('p.hint').remove();$("#login_div").hide()
$("#register_div").show()
$("#modal_head").show()
$('#login_register').modal('show');$.post('/jobs/applied_for/',{'job_id':$(this).attr('id')},function(data){},'json')})
jQuery(document).ready(function($){var offset=100,offset_opacity=1200,login_popup_capacity=2610
scroll_top_duration=500,$back_to_top=$('.cd-top');$login_block=$('.login_popup_block');$(window).scroll(function(){($(this).scrollTop()>offset)?$back_to_top.addClass('cd-is-visible'):$back_to_top.removeClass('cd-is-visible cd-fade-out');if($(this).scrollTop()>offset_opacity){$back_to_top.addClass('cd-fade-out');}
($(this).scrollTop()>offset)?$login_block.addClass('cd-is-visible'):$back_to_top.removeClass('cd-is-visible cd-fade-out');if($(this).scrollTop()>login_popup_capacity){$login_block.addClass('cd-fade-out');}});$back_to_top.on('click',function(event){event.preventDefault();$('body,html').animate({scrollTop:0,},scroll_top_duration);});});$('.adv_job_type').click(function(e){job_type=$(this).val()
if(job_type=='Walk-in'){$('.walkin_div').removeClass('advanced_search');$('.walkin_div').addClass('display_advanced_search');}
else{$('.walkin_div').removeClass('display_advanced_search');$('.walkin_div').addClass('advanced_search');}})
$("select#walkin_type").on('change',function(e){walkin_type=$('#walkin_type').val()
if(walkin_type=='custom_range'){$('.custom_range').show();}
else{$('.custom_range').hide();}});$('.search_location').change(function(e){$('#job_location').val($('.search_location').val())
var pad_lft=$('.select2-container--default .select2-selection--single').width()+20;$('#q-field').css('padding-left',pad_lft+'px')
var width_result=$('.banner_content').width()-pad_lft-90;$('.ac-skillresults, .ac-cityresults').css({'left':pad_lft-13+'px','width':width_result+'px'})})
$('.select2').select2();$("select#user_register_technical_skills").select2({placeholder:"Choose required Skillset",maximumSelectionSize:6});$("select#user_register_current_city").select2({placeholder:"Choose current location",'positionDropdown':true})
$('.select2').click(function(e){e.stopPropagation();$('.overlay_div').toggleClass('active_drop_down');})
$('body').click(function(e){$('.overlay_div').removeClass('active_drop_down');})
var AutocompleteCity=function(options){this.form_selector=options.form_selector
this.url='/search/city-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=parseInt(options.minimum_length||1)
this.form_elem=null
this.query_box=null}
AutocompleteCity.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=location]')
this.query_box.on('keyup',function(){var query=self.query_box.val().split(', ').slice(-1)[0]
var text=self.query_box.val()
if(query.length<self.minimum_length){$('.ac-cityresults').remove()
return false}
self.fetch(query,text)})
this.form_elem.on('click','.ac-cityresult',function(ev){id=$(this).parent('div').parent('div').siblings('input').attr('id')
old_str=$('#'+id).val();if(old_str.lastIndexOf(', ')>0){$('#'+id).val(old_str.substr(0,old_str.lastIndexOf(', ')+2)+$(this).text()+', ');}
else{$('#'+id).val($(this).text()+', ');}
SetCaretAtEnd(document.getElementById(id))
$('.ac-cityresults').remove()
return false})}
AutocompleteCity.prototype.fetch=function(query,text){var self=this
$.ajax({url:'/city-auto/',data:{'location':query,'text':text},success:function(data){self.show_results(data)}})}
AutocompleteCity.prototype.show_results=function(data){$('.ac-cityresults').remove()
var results=data.results||[]
var results_wrapper=$('<div class="ac-cityresults"></div>')
var base_elem=$('<div class="result-wrapper"><a href="/" aria-label="go to home page" class="ac-result"></a><br><p class="auther"></p></div>')
if(results.length>0){for(var res_offset in results){elem=$('<div class="result-wrapper"><a href="/" aria-label="go to home page" class="ac-cityresult"><span>'+results[res_offset]['name']+'</span></a></div>');results_wrapper.append(elem);}}
else{return false}
this.query_box.after(results_wrapper)}
var AutocompleteIndustry=function(options){this.form_selector=options.form_selector
this.url='/search/industry-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=parseInt(options.minimum_length||1)
this.form_elem=null
this.query_box=null}
AutocompleteIndustry.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=industry]')
this.query_box.on('keyup',function(){var query=self.query_box.val()
if(query.length<self.minimum_length){$('.ac-industryresults').remove()
return false}
self.fetch(query)})
this.form_elem.on('click','.ac-industryresult',function(ev){old_str=document.getElementsByName("industry")[0].value;if(old_str.lastIndexOf(', ')>0){document.getElementsByName("industry")[0].value=old_str.substr(0,old_str.lastIndexOf(', ')+2)+$(this).text()+', ';}
else{document.getElementsByName("industry")[0].value=$(this).text()+', ';}
$('.ac-industryresults').remove()
return false})}
AutocompleteIndustry.prototype.fetch=function(query){var self=this
$.ajax({url:this.url,data:{'industry':query},success:function(data){self.show_results(data)}})}
AutocompleteIndustry.prototype.show_results=function(data){$('.ac-industryresults').remove()
var results=data.results||[]
var results_wrapper=$('<div class="ac-industryresults"></div>')
var base_elem=$('<div class="result-wrapper"><a href="/" aria-label="go to home page" class="ac-result"></a><br><p class="auther"></p></div>')
if(results.length>0){for(var res_offset in results){elem=$('<div class="result-wrapper"><a href="/" aria-label="go to home page" class="ac-industryresult"><span>'+results[res_offset]['name']+'</span></a></div>');results_wrapper.append(elem);}}
else{return false}
this.query_box.after(results_wrapper)}
var AutocompleteFunctionalArea=function(options){this.form_selector=options.form_selector
this.url='/search/functional-area-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=parseInt(options.minimum_length||1)
this.form_elem=null
this.query_box=null}
AutocompleteFunctionalArea.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=functional_area]')
this.query_box.on('keyup',function(){var query=self.query_box.val()
if(query.length<self.minimum_length){$('.ac-functionalarearesults').remove()
return false}
self.fetch(query)})
this.form_elem.on('click','.ac-functionalarearesult',function(ev){old_str=document.getElementsByName("functional_area")[0].value;if(old_str.lastIndexOf(', ')>0){document.getElementsByName("functional_area")[0].value=old_str.substr(0,old_str.lastIndexOf(', ')+2)+$(this).text()+', ';}
else{document.getElementsByName("functional_area")[0].value=$(this).text()+', ';}
$('.ac-functionalarearesults').remove()
return false})}
AutocompleteFunctionalArea.prototype.fetch=function(query){var self=this
$.ajax({url:this.url,data:{'functional_area':query},success:function(data){self.show_results(data)}})}
AutocompleteFunctionalArea.prototype.show_results=function(data){$('.ac-functionalarearesults').remove()
var results=data.results||[]
var results_wrapper=$('<div class="ac-functionalarearesults"></div>')
var base_elem=$('<div class="result-wrapper"><a href="/" aria-label="go to home page" class="ac-result"></a><br><p class="auther"></p></div>')
if(results.length>0){for(var res_offset in results){elem=$('<div class="result-wrapper"><a href="/" aria-label="go to home page" class="ac-functionalarearesult"><span>'+results[res_offset]['name']+'</span></a></div>');results_wrapper.append(elem);}}
else{return false}
this.query_box.after(results_wrapper)}
$(document).ready(function(){window.autocompleteCity=new AutocompleteCity({form_selector:'.autocomplete-me'})
window.autocompleteCity.setup()
window.autocompleteAdvCity=new AutocompleteCity({form_selector:'.adv-autocomplete-me'})
window.autocompleteAdvCity.setup()
window.AutocompleteIndustry=new AutocompleteIndustry({form_selector:'.adv-autocomplete-me'})
window.AutocompleteIndustry.setup()
window.AutocompleteFunctionalArea=new AutocompleteFunctionalArea({form_selector:'.adv-autocomplete-me'})
window.AutocompleteFunctionalArea.setup()})
function SetCaretAtEnd(elem){var elemLen=elem.value.length;if(document.selection){elem.focus();var oSel=document.selection.createRange();oSel.moveStart('character',-elemLen);oSel.moveStart('character',elemLen);oSel.moveEnd('character',0);oSel.select();}
else if(elem.selectionStart||elem.selectionStart=='0'){elem.selectionStart=elemLen;elem.selectionEnd=elemLen;elem.focus();}}
$('.down_btn').mouseenter(function(e){scrollUp();});$('.up_btn').mouseenter(function(e){scrollDown();})
$('.down_btn, .up_btn').mouseleave(function(e){scrollStop();})
function scrollStop(){$('.drop_down ul').stop()}
function scrollUp(){$('.drop_down ul').animate({scrollTop:'+=10%'},150,scrollUp);}
function scrollDown(){$('.drop_down ul').animate({scrollTop:'-=10%'},150,scrollDown);}
$('body').click(function(e){$('.drop_down, .overlay_div').removeClass('active_drop_down');$('.ac-cityresults').remove(),$('.ac-skillresults').remove()
$('.ac-industryresults').remove()
$('.ac-functionalarearesults').remove()})
var Autocomplete=function(options){this.form_selector=options.form_selector
this.url='/search/skill-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=parseInt(options.minimum_length||1)
this.form_elem=null
this.query_box=null}
Autocomplete.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=q]')
this.query_box.on('keyup',function(){var query=self.query_box.val().split(', ').slice(-1)[0]
var search=self.query_box.val()
if(query.trim().length<self.minimum_length){$('.ac-skillresults').remove()
return false}
self.fetch(query,search)})
this.form_elem.on('click','.ac-result',function(ev){id=$(this).parent('div').parent('div').siblings('input[name=q]').attr('id')
old_str=$('#'+id).val();if(old_str.lastIndexOf(', ')>0){$('#'+id).val(old_str.substr(0,old_str.lastIndexOf(', ')+2)+$(this).text()+', ');}
else{$('#'+id).val($(this).text()+', ');}
SetCaretAtEnd(document.getElementById(id))
$('.ac-skillresults').remove()
return false})}
Autocomplete.prototype.fetch=function(query,search){var self=this
$.ajax({url:'/skill-auto/',data:{'q':query,'text':search},success:function(data){self.show_results(data)}})}
Autocomplete.prototype.show_results=function(data){$('.ac-skillresults').remove()
var results=data.results||[]
var results_wrapper=$('<div class="ac-skillresults"></div>')
var base_elem=$('<div class="result-wrapper"><a href="/" aria-label="go to home page" class="ac-result"></a><br><p class="auther"></p></div>')
if(results.length>0){for(var res_offset in results){elem=$('<div class="result-wrapper"><a href="/" aria-label="go to home page" class="ac-result" data-href="'+results[res_offset]['slug']+'" id="'+results[res_offset]['id']+'"><span>'+results[res_offset]['name']+'</span></a></div>');results_wrapper.append(elem);}}
else{return false}
this.query_box.after(results_wrapper)}
$(document).ready(function(){window.autocomplete=new Autocomplete({form_selector:'.autocomplete-me'})
window.autocomplete.setup()
window.autocompleteSkill=new Autocomplete({form_selector:'.adv-autocomplete-me'})
window.autocompleteSkill.setup()})
$('.content_wrap_list, .content_wrap').click(function(e){$('.ac-cityresults').remove(),$('.ac-skillresults').remove()
$('.ac-industryresults').remove()
$('.ac-functionalarearesults').remove()
$('.ac-educationresults').remove()});$('form#BaseSubscribeform').ajaxForm({type:'POST',dataType:'json',url:'/user_subscribe/',data:$('#BaseSubscribeform').serialize(),success:function(data){console.log(data)
if(data.error==false){open_dialog_with_url('Your email is successfully subscribed','Success!','.')}else if(data.response){$('p.hint').remove();for(var key in data.response){$('#subscribe_'+key).parent().after('<p class="hint">'+data.response[key]+'</p>');}}
else{$('#subscribe_response_message').html('<p class="hint">'+data.response_message+'</p>');}}});$('form#Jobsubscribeform').ajaxForm({type:'POST',dataType:'json',data:$('#subscribeform').serialize(),url:'/user_subscribe/',success:function(data){if(data.error==false){open_dialog_with_url('Your email is successfully subscribed','Success!','.')}else if(data.response){$('p.hint').remove();for(var key in data.response){if(key=='skill'){$('.skill_err').html('<p class="hint">'+data.response[key]+'</p>');}
else{$('#job_'+key).after('<p class="hint">'+data.response[key]+'</p>');}}}
else{$('p.hint').remove();$('#job_response_message').html('<p class="hint">'+data.response_message+'</p>');}}});$('.job_type').click(function(e){e.preventDefault();$('.job_type').removeClass('active_button');$('.job_type').parent().removeClass('active');$('#job_type').val($(this).attr('id'));$(this).addClass('active_button');$(this).parent().addClass('active');$('#job_type').val($(this).attr('id'));});$('input').keydown(function(e){if(e.keyCode==13){$(this).closest('form').submit();}});$(document).ready(function(){$("select#preferred_skills").select2({placeholder:"Select here",maximumSelectionSize:6,'positionDropdown':true});$($('.slide_bar_fill')).each(function(i,o){$(o).css('width',parseInt($(o).attr('id'))+'%')});$("#profile_span li").click(function(e){e.preventDefault();var pathname=window.location.pathname;if(pathname!='/profile/'){window.location='/profile?goto='+$(this).attr('id');}
else{id=$(this).attr('id')
$(window).scrollTop($('#div_'+id).offset().top-280);}})
$(".js-example-basic-single").select2();$(".dropdown").hover(function(){$('.dropdown-menu',this).fadeIn("fast");},function(){$('.dropdown-menu',this).fadeOut("fast");});});$("#walkin_from_date").datepicker({changeMonth:true,changeYear:true,yearRange:"2015:2050"})
$("#walkin_to_date").datepicker({changeMonth:true,changeYear:true,yearRange:"2015:2050"})
$(window).scroll(function(){if($(this).scrollTop()>1){$('header').addClass("sticky");}
else{$('header').removeClass("sticky");}});var AutocompleteRefineSkill=function(options){this.form_selector=options.form_selector
this.url='/search/skill-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=parseInt(options.minimum_length||1)
this.form_elem=null
this.query_box=null}
AutocompleteRefineSkill.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=q]')
this.query_box.on('keyup',function(){var query=self.query_box.val().split(', ').slice(-1)[0]
if(query.length<self.minimum_length){$('.ac-skillresults').remove()
return false}
self.fetch(query)})}
AutocompleteRefineSkill.prototype.fetch=function(query){var self=this
var text=''
$.each($("input[name='refine_skill']:checked"),function(){text=text+$(this).val()+', '})
$.ajax({url:'/skill-auto/',data:{'q':query,'search':'filter','text':text,},success:function(data){self.show_results(data)}})}
AutocompleteRefineSkill.prototype.show_results=function(data){$('.ac-skillresults').remove()
var results=data.results||[]
var results_wrapper=this.query_box.parent().siblings('ul')
if(results.length>0){$('input.refine_skill:not(:checked)').parent().remove();for(var res_offset in results){elem=$('<li class="list-group-item"><input type="checkbox" class="refine_search refine-skill refine_skill" name="refine_skill" value="'+results[res_offset]['name']+'">'+results[res_offset]['name']+'('+results[res_offset]['jobs_count']+')</li>');results_wrapper.append(elem);}}
else{return false}}
var AutocompleteRefineLocation=function(options){this.form_selector=options.form_selector
this.url='/search/skill-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=parseInt(options.minimum_length||1)
this.form_elem=null
this.query_box=null}
AutocompleteRefineLocation.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=location]')
this.query_box.on('keyup',function(){var query=self.query_box.val().split(', ').slice(-1)[0]
if(query.length<self.minimum_length){$('.ac-skillresults').remove()
return false}
self.fetch(query)})}
AutocompleteRefineLocation.prototype.fetch=function(query){var self=this
var text=''
$.each($("input[name='refine_location']:checked"),function(){text=text+$(this).val()+', '})
$.ajax({url:'/city-auto/',data:{'location':query,'search':'filter','text':text,},success:function(data){self.show_results(data)}})}
AutocompleteRefineLocation.prototype.show_results=function(data){$('.ac-skillresults').remove()
var results=data.results||[]
var results_wrapper=this.query_box.parent().siblings('ul')
if(results.length>0){$('input.refine_location:not(:checked)').parent().remove();for(var res_offset in results){elem=$('<li class="list-group-item"><input type="checkbox" class="refine_search refine-skill refine_location" name="refine_location" value="'+results[res_offset]['name']+'">'+results[res_offset]['name']+'('+results[res_offset]['jobs_count']+')</li>');results_wrapper.append(elem);}}
else{return false}}
var AutocompleteRefineIndustry=function(options){this.form_selector=options.form_selector
this.url='/search/industry-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=parseInt(options.minimum_length||1)
this.form_elem=null
this.query_box=null}
AutocompleteRefineIndustry.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=industry]')
this.query_box.on('keyup',function(){var query=self.query_box.val().split(', ').slice(-1)[0]
if(query.length<self.minimum_length){$('.ac-skillresults').remove()
return false}
self.fetch(query)})}
AutocompleteRefineIndustry.prototype.fetch=function(query){var self=this
$.ajax({url:'/search/industry-auto/',data:{'industry':query},success:function(data){self.show_results(data)}})}
AutocompleteRefineIndustry.prototype.show_results=function(data){$('.ac-skillresults').remove()
var results=data.results||[]
var results_wrapper=this.query_box.parent().siblings('ul')
if(results.length>0){$('input.refine_industry:not(:checked)').parent().remove();for(var res_offset in results){elem=$('<li class="list-group-item"><input type="checkbox" class="refine_search refine-skill refine_industry" name="refine_industry" value="'+results[res_offset]['name']+'">'+results[res_offset]['name']+'('+results[res_offset]['jobs_count']+')</li>');results_wrapper.append(elem);}}
else{return false}}
var AutocompleteRefineQualification=function(options){this.form_selector=options.form_selector
this.url='/search/education-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=1
this.form_elem=null
this.query_box=null}
AutocompleteRefineQualification.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=education]')
this.query_box.on('keyup',function(){var query=self.query_box.val()
if(query.length<self.minimum_length){$('.ac-educationresults').remove()
return false}
self.fetch(query)})}
AutocompleteRefineQualification.prototype.fetch=function(query){var self=this
$.ajax({url:'/search/education-auto/',data:{'education':query},success:function(data){self.show_results(data)}})}
AutocompleteRefineQualification.prototype.show_results=function(data){$('.ac-educationresults').remove()
var results=data.results||[]
var results_wrapper=this.query_box.parent().siblings('ul')
if(results.length>0){$('input.refine_edu:not(:checked)').parent().remove();for(var res_offset in results){elem=$('<li class="list-group-item"><input type="checkbox" class="refine_search refine-edu refine_edu" name="refine_edu" value="'+results[res_offset]['name']+'">'+results[res_offset]['name']+'('+results[res_offset]['jobs_count']+')</li>');results_wrapper.append(elem);}}
else{return false}}
var AutocompleteRefineState=function(options){this.form_selector=options.form_selector
this.url='/search/state-auto/'||options.url
this.delay=parseInt(options.delay||300)
this.minimum_length=1
this.form_elem=null
this.query_box=null}
AutocompleteRefineState.prototype.setup=function(){var self=this
this.form_elem=$(this.form_selector)
this.query_box=this.form_elem.find('input[name=state]')
this.query_box.on('keyup',function(){console.log('enter')
var query=self.query_box.val()
if(query.length<self.minimum_length){$('.ac-stateresults').remove()
return false}
self.fetch(query)})}
AutocompleteRefineState.prototype.fetch=function(query){var self=this
var text=''
$.each($("input[name='refine_state']:checked"),function(){text=text+$(this).val()+', '})
$.ajax({url:'/search/state-auto/',data:{'state':query,'text':text},success:function(data){self.show_results(data)}})}
AutocompleteRefineState.prototype.show_results=function(data){$('.ac-stateresults').remove()
var results=data.results||[]
var results_wrapper=this.query_box.parent().siblings('ul')
if(results.length>0){$('input.refine_state:not(:checked)').parent().remove();for(var res_offset in results){elem=$('<li class="list-group-item"><input type="checkbox" class="refine_search refine-state refine_state" name="refine_state" value="'+results[res_offset]['name']+'">'+results[res_offset]['name']+'('+results[res_offset]['jobs_count']+')</li>');results_wrapper.append(elem);}}
else{return false}}
$(document).ready(function(){window.autocompleteRefineSkill=new AutocompleteRefineSkill({form_selector:'.refine-autocomplete-me'})
window.autocompleteRefineSkill.setup()
window.autocompleteRefineLocation=new AutocompleteRefineLocation({form_selector:'.refine-autocomplete-me'})
window.autocompleteRefineLocation.setup()
window.autocompleteRefineIndustry=new AutocompleteRefineIndustry({form_selector:'.refine-autocomplete-me'})
window.autocompleteRefineIndustry.setup()
window.autocompleteRefineQualification=new AutocompleteRefineQualification({form_selector:'.refine-autocomplete-me'})
window.autocompleteRefineQualification.setup()
window.autocompleteRefineState=new AutocompleteRefineState({form_selector:'.refine-autocomplete-me'})
window.autocompleteRefineState.setup()
$('select#job_skills').select2({'placeholder':'Select Skills'})})
$('body').on("click",".refine_search",function(e){$('#refine_search').val('True');$(".se-pre-con").show()
if($("input[name=job_type]").val()=='Fresher'){window.location='/Fresher-jobs/'
return}
$('#login_register').block();$('#refine-search').submit();});$('.skip').click(function(e){e.preventDefault();current_block=$('.skip_block.show');if($(current_block).next('.skip_block').length>0){$(current_block).next('.skip_block').removeClass('hide').addClass('show');$(current_block).removeClass('show').addClass('hide');;}
else{$(".skip_close_tour").hide();}});$('.close_tour').click(function(e){e.preventDefault();$(".skip_close_tour").hide();});$("span.apply").click(function(e){e.preventDefault();$.post('/jobs/apply/'+$(this).attr('id')+'/',{},function(data){if(data.error){if(data.url){open_dialog_with_url(data.response,'Error!!',data.url)}
else{open_dialog(data.response,'Error!!')}}else{open_dialog_with_url(data.response,'Success!!',data.url)}},'json');});$('span.apply_job').click(function(e){$.post('/jobs/applied_for/',{'job_id':$(this).attr('id')},function(data){if(data.error){}else{$('#login_register').modal('show');}},'json')});$("a.applicant_apply").click(function(e){e.preventDefault();href=$(this).attr('data-href')
id=$(this).attr('id')
$.post('/jobs/apply/'+$(this).attr('id')+'/',{},function(data){if(data.error){if(data.url){open_dialog_with_url(data.response,'Error!',data.url)}
else{open_dialog(data.response,'Error!')}}else{$("#block_job_apply").text(data.response)
$("#block_job_apply").dialog({modal:true,title:"Info!",draggable:false,buttons:[{text:"OK",click:function(){window.location=data.url;}}]});$('.ui-dialog-titlebar-close').html('<span>X</span>')
$('.ui-dialog-titlebar-close').click(function(){$("#"+id).text('Applied')})}},'json');});$(".job_list_section .job_item").click(function(e){if($(e.target).is('.job_apply #location_span')){e.preventDefault();return;}
window.open($(this).find(".job_url").attr("href"),'_blank')})
$(".job_list_section .job_item a").click(function(e){e.stopPropagation();})
$(".job_list_section .job_item").hover(function(){$(this).css('cursor','pointer');},function(){$(this).css('cursor','auto');});$("#other_location").click(function(e){$(this).parent().find('.hint').remove()
if($(this).is(":checked")){$(this).parent().find('.select2').hide()
$("#user_register_other_location").show()}
else{$(this).parent().find('.select2').show()
$("#user_register_other_location").hide()}})
$("form#jobseeker_educationform").submit(function(e){e.preventDefault();$.post("/education/add/",$("form#jobseeker_educationform").serialize(),function(data){if(data.error){if(data.response_message){open_dialog(data.response_message,'Error!')}
$('p.hint').remove();for(var key in data.response){if(key=='from_date'|key=='to_date'|key=='current_education'){$('#ed_'+key).parent().append('<p class="hint">'+data.response[key]+'</p>');}
else{$('#'+key).parent().append('<p class="hint">'+data.response[key]+'</p>');}}}else{if(applying_for_job=true){$("#candidate_educationform").hide()
$("#candidate_projectform").show()
$('#modal_head').text('PROJECT DETAILS')}}},'json');});$("form#jobseeker_projectform").submit(function(e){e.preventDefault();$.post("/project/add/",$("form#jobseeker_projectform").serialize(),function(data){if(data.error){$('p.hint').remove();if(data.response_message){open_dialog(data.response_message,'Info!')}
for(var key in data.response){if(key=="name"){$('#project_'+key).parent().append('<p class="hint">'+data.response[key]+'</p>');}
else{$('#'+key).parent().append('<p class="hint">'+data.response[key]+'</p>');}}}else{if(applying_for_job=true){$('#candidate_projectform').hide()
$('#candidate_resumeform').show()
$('#modal_head').text('Upload Resume')}}},'json');});$(function(){$("#from_date").datepicker({changeMonth:true,changeYear:true,yearRange:"1950:2050"});});$(function(){$("#to_date").datepicker({changeMonth:true,changeYear:true,yearRange:"1950:2050"});});$(function(){$("#ed_from_date").datepicker({changeMonth:true,changeYear:true,yearRange:"1950:2050"});});$(function(){$("#ed_to_date").datepicker({changeMonth:true,changeYear:true,yearRange:"1950:2050"});});$('#city').select2();$('form#jobseeker_resumeform').ajaxForm({type:'POST',dataType:'json',data:$('#jobseeker_resumeform').serialize(),url:'/upload_resume/',success:function(data){$.get('/jobs/job_apply/'+job_id+'/',{'apply_now':'True'},function(data)
{var url=job_apply_url.split('/')[1]
window.location='/'+url+'/?applied'},'json')}});$('#ed_current_education').click(function(e){if($('#ed_current_education').is(":checked")){$("#ed_to_date").val('');$("#ed_to_date").attr("disabled","disabled");}
else{$("#ed_to_date").removeAttr("disabled");}});$("select#skills").select2({placeholder:"Skills Used",maximumSelectionSize:6});$(".form_cancel").click(function(e){var url=job_apply_url.split('/')[1]
window.location='/'+url+'/?job_apply=apply'});$(".form_submit").on("click",function(){$('#login_register').scrollTop(0);});;