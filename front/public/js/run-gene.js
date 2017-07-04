var gene={},input={},geneLoaded=false;
let classPerDay=12;
function loadGenes(callback) {
    if(!geneLoaded) {
        geneLoaded=true;
        $.ajax({
            dataType: "json",
            url: "/api/gene/"+id+"/"+gen,
            success: function(genes) {
                $.ajax({
                    dataType: "json",
                    url: "/api/input/"+id,
                    success: function(inputs) {
                        gene=genes,input=inputs;
                        callback();
                    }
                });
            }
        });
    }
    else callback();
}
function clearTable() {
    for(var i=1;i<13;i++) {
        $('#tt-mon-'+i.toString()).html("");
        $('#tt-tue-'+i.toString()).html("");
        $('#tt-wed-'+i.toString()).html("");
        $('#tt-thu-'+i.toString()).html("");
        $('#tt-fri-'+i.toString()).html("");
    }
}
function dayString(num) {
    switch(Math.floor(num/classPerDay)) {
        case 0:
            return 'mon';
        case 1:
            return 'tue';
        case 2:
            return 'wed';
        case 3:
            return 'thu';
        case 4:
            return 'fri';
    }
}
function dayStringKor(num) {
    switch(Math.floor(num/classPerDay)) {
        case 0:
            return '월';
        case 1:
            return '화';
        case 2:
            return '수';
        case 3:
            return '목';
        case 4:
            return '금';
    }
}
function drawGene(no) {
    clearTable();
    myGene=gene[parseInt(no)].genePairs;
    $('#div-gene-summary-title').html('유전자 정보 - '+(no+1).toString()+'번 유전자');
    $('#div-gene-summary').html('<h4>점수: '+gene[parseInt(no)].geneScore+'<h4/>');
    for(var cl in myGene) {
        console.log();
        var ds=dayString(myGene[cl][0]),myColor=randomColor({luminosity: 'dark'}),cname=input["subjects"][cl].name,room=input["subjects"][cl].room;
        $('#div-gene-summary').html($('#div-gene-summary').html()+"<p class='p-table-class' style='font-weight: bold; color: "+myColor+";'>"+cname+' ('+dayStringKor(myGene[cl][0])+' '+(myGene[cl][0]%classPerDay+1)+'~'+(myGene[cl][1]%classPerDay+1)+"교시)</p>");
        for(var i=(myGene[cl][0]%classPerDay+1);i<=(myGene[cl][1]%classPerDay+1);i++) {
            $('#tt-'+ds+'-'+i.toString()).html($('#tt-'+ds+'-'+i.toString()).html()+"<p class='p-table-class' style='font-weight: bold; color: "+myColor+";' data-id="+cl+">"+cname+"</p>");
            console.log(room);
            $('#tt-r'+room+'-'+ds+'-'+i.toString()).html($('#tt-r'+room+'-'+ds+'-'+i.toString()).html()+"<p class='p-table-class' style='font-weight: bold; color: "+myColor+";' data-id="+cl+">"+cname+"</p>");
        }
    }                    
}
window.onload = function() {
    $('.btn-gene-list').click(function() {
        var no=$(this).data('id');
        loadGenes(function() {
            drawGene(no);
        });
    });
    $(document).on("click", ".p-table-class",function() {
        window.open('/run-input/'+id+'#c'+$(this).data('id'), '_blank');
    });
}


// ===== Scroll to Top ==== 
$(window).scroll(function() {
    if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
});
$('#return-to-top').click(function() {      // When arrow is clicked
    $('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
});