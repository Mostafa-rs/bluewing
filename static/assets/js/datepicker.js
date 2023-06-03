
$("#startDatePicker").datepicker({
    dateFormat: 'yy-mm-dd',
    changeMonth: true,
    minDate: new Date(),
    maxDate: '+2Y',
    onSelect: function(date){

        var selectedDate = new Date(date);
        console.log(selectedDate)
        var msecsInADay = 172800000;
        var endDate = new Date(selectedDate.getTime() + 172800000);

       //Set Minimum Date of EndDatePicker After Selected Date of StartDatePicker
        $("#endDatePicker").datepicker( "option", "minDate", endDate );
       //  $("#endDatePicker").datepicker({
       //    dateFormat: 'yy-mm-dd',
       //    changeMonth: true,
       //    minDate: new Date(selectedDate.getTime() + endDate),
       //    maxDate: '+2y'
       //  })


    }
});

$("#endDatePicker").datepicker({
    dateFormat: 'yy-mm-dd',
    changeMonth: true,
    maxDate: '+2Y'
    // minDate: new Date(new Date().getTime() + 259200000)
});