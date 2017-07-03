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
function drawGene(no) {
    clearTable();
    //[{"genePairs":{"1":[0,7],"2":[18,25],"3":[27,34],"4":[37,44],"5":[37,44],"6":[9,16]},"geneScore":16},{"genePairs":{"1":[36,43],"2":[19,26],"3":[37,44],"4":[27,34],"5":[1,8],"6":[10,17]},"geneScore":21},{"genePairs":{"1":[19,26],"2":[0,7],"3":[9,16],"4":[10,17],"5":[18,25],"6":[9,16]},"geneScore":21},{"genePairs":{"1":[9,16],"2":[37,44],"3":[19,26],"4":[19,26],"5":[36,43],"6":[37,44]},"geneScore":30},{"genePairs":{"1":[37,44],"2":[9,16],"3":[36,43],"4":[27,34],"5":[28,35],"6":[36,43]},"geneScore":35},{"genePairs":{"1":[36,43],"2":[18,25],"3":[27,34],"4":[27,34],"5":[1,8],"6":[9,16]},"geneScore":16},{"genePairs":{"1":[0,7],"2":[19,26],"3":[37,44],"4":[27,34],"5":[1,8],"6":[10,17]},"geneScore":7},{"genePairs":{"1":[9,16],"2":[0,7],"3":[19,26],"4":[10,17],"5":[36,43],"6":[9,16]},"geneScore":14},{"genePairs":{"1":[19,26],"2":[0,7],"3":[9,16],"4":[10,17],"5":[36,43],"6":[37,44]},"geneScore":14}]
    myGene=gene[parseInt(no)].genePairs;
    for(var cl in myGene) {
        console.log();
        var ds=dayString(myGene[cl][0]),myColor=randomColor({luminosity: 'dark'}),cname=input["subjects"][cl].name;
        for(var i=(myGene[cl][0]%classPerDay);i<=(myGene[cl][1]%classPerDay);i++) {
            $('#tt-'+ds+'-'+i.toString()).html($('#tt-'+ds+'-'+i.toString()).html()+"<p class='p-table-class' style='font-weight: bold; color: "+myColor+";' data-id="+cl+">"+cname+"</p>");
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