function hideFormFieldTooltips(){
	// Need to be separated and not boud to hide event of modal dialog, since 
	// datepicker hide event would also trigger it and we don't want that.
	$('.form-field').tooltip('hide');
}

function loadDialog(){
	dialog_selector = "#editor-dialog"
	form_selector = "#editor-form"
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
		},
	})
}