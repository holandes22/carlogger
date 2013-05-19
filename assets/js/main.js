function hideFormFieldTooltips(){
	// Need to be separated and not boud to hide event of modal dialog, since 
	// datepicker hide event would also trigger it and we don't want that.
	$('.form-field').tooltip('hide');
}

function loadDialog(){
	dialog_selector = "#editor-dialog";
	form_selector = "#editor-form";
	success_url = $(form_selector).attr("success-url");
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			hideFormFieldTooltips();
			if(data.match("invalid_form")){
				// We got errors in form
				$(dialog_selector).html(data).modal('show');
				options = {trigger: 'manual', placement: 'right', container: '#editor-dialog'}
				$('.form-field').tooltip(options).tooltip('show');
				return false;
			}
			$(dialog_selector).modal('hide');
			window.location = success_url;
		},
		error: function(jqXHR, textStatus, errorThrown){
	    	$(dialog_selector).modal('hide');
    		$('#page_content').empty();
    		$('#error_alert').show();
    	}
	})
}

function loadDeleteConfirmDialog(){
	dialog_selector = "#warning-dialog";
	form_selector = "#warning-form";
	success_url = $(form_selector).attr("success-url");
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			$(dialog_selector).modal('hide');
			window.location = success_url;
		},
	    error: function(jqXHR, textStatus, errorThrown){
	    	$(dialog_selector).modal('hide');
    		$('#page_content').empty();
    		$('#error_alert').show();
    	}
	})	
}

function showTreatmentDetails(selector){
	$(selector).prev().toggleClass('icon-chevron-right').toggleClass('icon-chevron-down');
	$(selector).next().toggle();	
}

function showAllTreatmentDetails(){
	$("a.show-treatment-details").each(function(){
		showTreatmentDetails();
	})
}

$(document).ready(function () {
	$("a.show-treatment-details").on('click', null, function(e){
		showTreatmentDetails(this);
	})
})