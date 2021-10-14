// $( '#signup' ).click( function (){
//     $( '.pinkbox' ).css( 'transform', 'translateX(80%)' );
//     $( '.signin' ).addClass( 'nodisplay' );
//     $( '.signup' ).removeClass( 'nodisplay' );
// } );

// $( '#signin' ).click( function (){
//     $( '.pinkbox' ).css( 'transform', 'translateX(0%)' );
//     $( '.signup' ).addClass( 'nodisplay' );
//     $( '.signin' ).removeClass( 'nodisplay' );
// } );

function closeSnack(snackButton) {

    if (snackButton != null) {
        if (snackButton instanceof HTMLElement) {
            let snack = snackButton.parentElement;

            if (snack != null) {
                snack.classList.add("hide_snack");
            }
        }
    }
}