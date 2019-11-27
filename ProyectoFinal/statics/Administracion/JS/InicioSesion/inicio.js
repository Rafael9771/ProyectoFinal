function iniciar(){
    document.getElementById('formulario').setAttribute('action', '/admin/metodopost');
    document.getElementById('formulario').setAttribute('method', 'post');
    document.getElementById('formulario').submit();
}

function iniciarP(){
    document.getElementById('formulario').setAttribute('action', '/admin/adminP');
    document.getElementById('formulario').setAttribute('method', 'post');
    document.getElementById('formulario').submit();
}