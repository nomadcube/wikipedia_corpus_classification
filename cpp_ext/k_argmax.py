# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info

if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_k_argmax', [dirname(__file__)])
        except ImportError:
            import _k_argmax
            return _k_argmax
        if fp is not None:
            try:
                _mod = imp.load_module('_k_argmax', fp, pathname, description)
            finally:
                fp.close()
            return _mod


    _k_argmax = swig_import_helper()
    del swig_import_helper
else:
    import _k_argmax
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)


def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass


    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")

    __repr__ = _swig_repr
    __swig_destroy__ = _k_argmax.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _k_argmax.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _k_argmax.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _k_argmax.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _k_argmax.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _k_argmax.SwigPyIterator_equal(self, x)

    def copy(self):
        return _k_argmax.SwigPyIterator_copy(self)

    def next(self):
        return _k_argmax.SwigPyIterator_next(self)

    def __next__(self):
        return _k_argmax.SwigPyIterator___next__(self)

    def previous(self):
        return _k_argmax.SwigPyIterator_previous(self)

    def advance(self, n):
        return _k_argmax.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _k_argmax.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _k_argmax.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _k_argmax.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _k_argmax.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _k_argmax.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _k_argmax.SwigPyIterator___sub__(self, *args)

    def __iter__(self):
        return self


SwigPyIterator_swigregister = _k_argmax.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


class element_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, element_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, element_t, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _k_argmax.element_t_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _k_argmax.element_t___nonzero__(self)

    def __bool__(self):
        return _k_argmax.element_t___bool__(self)

    def __len__(self):
        return _k_argmax.element_t___len__(self)

    def pop(self):
        return _k_argmax.element_t_pop(self)

    def __getslice__(self, i, j):
        return _k_argmax.element_t___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _k_argmax.element_t___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _k_argmax.element_t___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _k_argmax.element_t___delitem__(self, *args)

    def __getitem__(self, *args):
        return _k_argmax.element_t___getitem__(self, *args)

    def __setitem__(self, *args):
        return _k_argmax.element_t___setitem__(self, *args)

    def append(self, x):
        return _k_argmax.element_t_append(self, x)

    def empty(self):
        return _k_argmax.element_t_empty(self)

    def size(self):
        return _k_argmax.element_t_size(self)

    def clear(self):
        return _k_argmax.element_t_clear(self)

    def swap(self, v):
        return _k_argmax.element_t_swap(self, v)

    def get_allocator(self):
        return _k_argmax.element_t_get_allocator(self)

    def begin(self):
        return _k_argmax.element_t_begin(self)

    def end(self):
        return _k_argmax.element_t_end(self)

    def rbegin(self):
        return _k_argmax.element_t_rbegin(self)

    def rend(self):
        return _k_argmax.element_t_rend(self)

    def pop_back(self):
        return _k_argmax.element_t_pop_back(self)

    def erase(self, *args):
        return _k_argmax.element_t_erase(self, *args)

    def __init__(self, *args):
        this = _k_argmax.new_element_t(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _k_argmax.element_t_push_back(self, x)

    def front(self):
        return _k_argmax.element_t_front(self)

    def back(self):
        return _k_argmax.element_t_back(self)

    def assign(self, n, x):
        return _k_argmax.element_t_assign(self, n, x)

    def resize(self, *args):
        return _k_argmax.element_t_resize(self, *args)

    def insert(self, *args):
        return _k_argmax.element_t_insert(self, *args)

    def reserve(self, n):
        return _k_argmax.element_t_reserve(self, n)

    def capacity(self):
        return _k_argmax.element_t_capacity(self)

    __swig_destroy__ = _k_argmax.delete_element_t
    __del__ = lambda self: None


element_t_swigregister = _k_argmax.element_t_swigregister
element_t_swigregister(element_t)


class result_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, result_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, result_t, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _k_argmax.result_t_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _k_argmax.result_t___nonzero__(self)

    def __bool__(self):
        return _k_argmax.result_t___bool__(self)

    def __len__(self):
        return _k_argmax.result_t___len__(self)

    def pop(self):
        return _k_argmax.result_t_pop(self)

    def __getslice__(self, i, j):
        return _k_argmax.result_t___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _k_argmax.result_t___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _k_argmax.result_t___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _k_argmax.result_t___delitem__(self, *args)

    def __getitem__(self, *args):
        return _k_argmax.result_t___getitem__(self, *args)

    def __setitem__(self, *args):
        return _k_argmax.result_t___setitem__(self, *args)

    def append(self, x):
        return _k_argmax.result_t_append(self, x)

    def empty(self):
        return _k_argmax.result_t_empty(self)

    def size(self):
        return _k_argmax.result_t_size(self)

    def clear(self):
        return _k_argmax.result_t_clear(self)

    def swap(self, v):
        return _k_argmax.result_t_swap(self, v)

    def get_allocator(self):
        return _k_argmax.result_t_get_allocator(self)

    def begin(self):
        return _k_argmax.result_t_begin(self)

    def end(self):
        return _k_argmax.result_t_end(self)

    def rbegin(self):
        return _k_argmax.result_t_rbegin(self)

    def rend(self):
        return _k_argmax.result_t_rend(self)

    def pop_back(self):
        return _k_argmax.result_t_pop_back(self)

    def erase(self, *args):
        return _k_argmax.result_t_erase(self, *args)

    def __init__(self, *args):
        this = _k_argmax.new_result_t(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _k_argmax.result_t_push_back(self, x)

    def front(self):
        return _k_argmax.result_t_front(self)

    def back(self):
        return _k_argmax.result_t_back(self)

    def assign(self, n, x):
        return _k_argmax.result_t_assign(self, n, x)

    def resize(self, *args):
        return _k_argmax.result_t_resize(self, *args)

    def insert(self, *args):
        return _k_argmax.result_t_insert(self, *args)

    def reserve(self, n):
        return _k_argmax.result_t_reserve(self, n)

    def capacity(self):
        return _k_argmax.result_t_capacity(self)

    __swig_destroy__ = _k_argmax.delete_result_t
    __del__ = lambda self: None


result_t_swigregister = _k_argmax.result_t_swigregister
result_t_swigregister(result_t)


class row_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, row_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, row_t, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _k_argmax.row_t_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _k_argmax.row_t___nonzero__(self)

    def __bool__(self):
        return _k_argmax.row_t___bool__(self)

    def __len__(self):
        return _k_argmax.row_t___len__(self)

    def pop(self):
        return _k_argmax.row_t_pop(self)

    def __getslice__(self, i, j):
        return _k_argmax.row_t___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _k_argmax.row_t___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _k_argmax.row_t___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _k_argmax.row_t___delitem__(self, *args)

    def __getitem__(self, *args):
        return _k_argmax.row_t___getitem__(self, *args)

    def __setitem__(self, *args):
        return _k_argmax.row_t___setitem__(self, *args)

    def append(self, x):
        return _k_argmax.row_t_append(self, x)

    def empty(self):
        return _k_argmax.row_t_empty(self)

    def size(self):
        return _k_argmax.row_t_size(self)

    def clear(self):
        return _k_argmax.row_t_clear(self)

    def swap(self, v):
        return _k_argmax.row_t_swap(self, v)

    def get_allocator(self):
        return _k_argmax.row_t_get_allocator(self)

    def begin(self):
        return _k_argmax.row_t_begin(self)

    def end(self):
        return _k_argmax.row_t_end(self)

    def rbegin(self):
        return _k_argmax.row_t_rbegin(self)

    def rend(self):
        return _k_argmax.row_t_rend(self)

    def pop_back(self):
        return _k_argmax.row_t_pop_back(self)

    def erase(self, *args):
        return _k_argmax.row_t_erase(self, *args)

    def __init__(self, *args):
        this = _k_argmax.new_row_t(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _k_argmax.row_t_push_back(self, x)

    def front(self):
        return _k_argmax.row_t_front(self)

    def back(self):
        return _k_argmax.row_t_back(self)

    def assign(self, n, x):
        return _k_argmax.row_t_assign(self, n, x)

    def resize(self, *args):
        return _k_argmax.row_t_resize(self, *args)

    def insert(self, *args):
        return _k_argmax.row_t_insert(self, *args)

    def reserve(self, n):
        return _k_argmax.row_t_reserve(self, n)

    def capacity(self):
        return _k_argmax.row_t_capacity(self)

    __swig_destroy__ = _k_argmax.delete_row_t
    __del__ = lambda self: None


row_t_swigregister = _k_argmax.row_t_swigregister
row_t_swigregister(row_t)


class all_row_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, all_row_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, all_row_t, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _k_argmax.all_row_t_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _k_argmax.all_row_t___nonzero__(self)

    def __bool__(self):
        return _k_argmax.all_row_t___bool__(self)

    def __len__(self):
        return _k_argmax.all_row_t___len__(self)

    def pop(self):
        return _k_argmax.all_row_t_pop(self)

    def __getslice__(self, i, j):
        return _k_argmax.all_row_t___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _k_argmax.all_row_t___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _k_argmax.all_row_t___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _k_argmax.all_row_t___delitem__(self, *args)

    def __getitem__(self, *args):
        return _k_argmax.all_row_t___getitem__(self, *args)

    def __setitem__(self, *args):
        return _k_argmax.all_row_t___setitem__(self, *args)

    def append(self, x):
        return _k_argmax.all_row_t_append(self, x)

    def empty(self):
        return _k_argmax.all_row_t_empty(self)

    def size(self):
        return _k_argmax.all_row_t_size(self)

    def clear(self):
        return _k_argmax.all_row_t_clear(self)

    def swap(self, v):
        return _k_argmax.all_row_t_swap(self, v)

    def get_allocator(self):
        return _k_argmax.all_row_t_get_allocator(self)

    def begin(self):
        return _k_argmax.all_row_t_begin(self)

    def end(self):
        return _k_argmax.all_row_t_end(self)

    def rbegin(self):
        return _k_argmax.all_row_t_rbegin(self)

    def rend(self):
        return _k_argmax.all_row_t_rend(self)

    def pop_back(self):
        return _k_argmax.all_row_t_pop_back(self)

    def erase(self, *args):
        return _k_argmax.all_row_t_erase(self, *args)

    def __init__(self, *args):
        this = _k_argmax.new_all_row_t(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _k_argmax.all_row_t_push_back(self, x)

    def front(self):
        return _k_argmax.all_row_t_front(self)

    def back(self):
        return _k_argmax.all_row_t_back(self)

    def assign(self, n, x):
        return _k_argmax.all_row_t_assign(self, n, x)

    def resize(self, *args):
        return _k_argmax.all_row_t_resize(self, *args)

    def insert(self, *args):
        return _k_argmax.all_row_t_insert(self, *args)

    def reserve(self, n):
        return _k_argmax.all_row_t_reserve(self, n)

    def capacity(self):
        return _k_argmax.all_row_t_capacity(self)

    __swig_destroy__ = _k_argmax.delete_all_row_t
    __del__ = lambda self: None


all_row_t_swigregister = _k_argmax.all_row_t_swigregister
all_row_t_swigregister(all_row_t)


def construct_all_row(arg1, arg2, arg3):
    return _k_argmax.construct_all_row(arg1, arg2, arg3)


construct_all_row = _k_argmax.construct_all_row


def k_argmax_per_row(arg1):
    return _k_argmax.k_argmax_per_row(arg1)


k_argmax_per_row = _k_argmax.k_argmax_per_row


def k_argmax(arg1, arg2, arg3):
    return _k_argmax.k_argmax(arg1, arg2, arg3)


k_argmax = _k_argmax.k_argmax
# This file is compatible with both classic and new-style classes.
