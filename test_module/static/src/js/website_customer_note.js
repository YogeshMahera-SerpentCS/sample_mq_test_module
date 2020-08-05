odoo.define("test_module.payment", function(require) {
    "use strict";

    var ajax = require("web.ajax");
    $(document).ready(function() {
        $("button#o_payment_form_pay").bind("click", function() {
            var customer_note = $("#note2").val();
            ajax.jsonRpc("/notes", "call", {
                note2: customer_note,
            });
        });
    });
});
