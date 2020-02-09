import os
import re
from math import factorial
from jinja2 import FileSystemLoader, Environment


def jinja(template_file, data):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    loader = FileSystemLoader(dir_path + '/templates')
    template = Environment(loader=loader).get_template(template_file)
    code = template.render(data)
    code = re.sub(r'\n\s*\n', '\n', code)
    return code


def port_pca(pca):
    return jinja('pca/pca.jinja', {
        'X_DIM': pca.components_.shape[1],
        'PCA_DIM': pca.components_.shape[0],
        'F': {
            'round': round
        },
        'pca_components': pca.components_,
    })


def port(clf,
         pca=None,
         test_set=None,
         classmap=None,
         platform='arduino',
         **kwargs):
    assert type(clf).__name__ == 'SVC', 'Only sklearn.svm.SVC is supported for now'
    assert isinstance(clf.gamma, float)
    support_v = clf.support_vectors_
    n_classes = len(clf.n_support_)
    pca_code = port_pca(pca) if pca is not None else ''
    template_data = {
        'KERNEL_TYPE': clf.kernel,
        'KERNEL_GAMMA': clf.gamma,
        'KERNEL_COEF': clf.coef0,
        'KERNEL_DEGREE': clf.degree,
        'FEATURES_DIM': len(support_v[0]),
        'VECTORS_COUNT': len(support_v),
        'CLASSES_COUNT': n_classes,
        'DECISIONS_COUNT': n_classes * (n_classes - 1) // 2,
        'ORIGINAL_FEATURES_DIM': len(support_v[0]) if pca is None else len(pca[0]),
        'support_v': support_v,
        'n_support': clf.n_support_,
        'intercepts': clf.intercept_,
        'coefs': clf.dual_coef_,
        'X': test_set[0] if test_set else None,
        'y': test_set[1] if test_set else None,
        'classmap': classmap,
        'pca_code': pca_code,
        'F': {
            'enumerate': enumerate,
            'round': round
        },
        'isAttiny': platform == 'attiny',
    }
    return jinja('svm.jinja', template_data)
