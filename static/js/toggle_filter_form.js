document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('filter-form');
    var icon = document.getElementById('filter-icon');

    // Check sessionStorage for the form's visibility
    var isFormVisible = sessionStorage.getItem('isFormVisible');

    if (isFormVisible === 'true') {
        form.style.display = 'flex';
    } else {
        form.style.display = 'none';
    }

    // Toggle form visibility on icon click
    icon.addEventListener('click', function() {
        form.style.display = (form.style.display === 'none' || form.style.display === '') ? 'flex' : 'none';

        // Update sessionStorage with the current form visibility
        sessionStorage.setItem('isFormVisible', form.style.display === 'flex');
    });

    // Handle page unload event
    window.addEventListener('beforeunload', function() {
        // Set sessionStorage to hide the form when leaving the page
        sessionStorage.setItem('isFormVisible', 'flex');
    });
});


//Date picker
$(function() {
    $('input[name="dates"]').daterangepicker({
        opens: 'left'
    },
    function(start, end, label) {
        $('#id_date_created_0').val(start.format('YYYY-MM-DD'))
        $('#id_date_created_1').val(end.format('YYYY-MM-DD'))
    });
    $('#datePicker').removeAttr('name');
});