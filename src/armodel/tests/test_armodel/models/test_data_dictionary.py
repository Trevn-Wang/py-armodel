import pytest

from ....models.data_dictionary import SwDataDefProps, SwPointerTargetProps
from ....models.general_structure import ARObject

class Test_M2_MSR_DataDictionary_DataDefProperties:
    def test_SwDataDefProps(self):
        props = SwDataDefProps()

        assert(isinstance(props, ARObject))
        assert(isinstance(props, SwDataDefProps))

        assert(props.base_type_ref == None)
        assert(props.compu_method_ref == None)
        assert(props.data_constr_ref == None)                 
        assert(props.implementation_data_type_ref == None)
        assert(props.sw_impl_policy == None)
        assert(props.sw_calibration_access == '')
        assert(props.sw_pointer_target_props == None)

    def test_SwPointerTargetProps(self):
        props = SwPointerTargetProps()

        assert(isinstance(props, ARObject))
        assert(isinstance(props, SwPointerTargetProps))

        assert(props.function_pointer_signature == None)
        assert(props.sw_data_def_props == None)
        assert(props.target_category == "")