 {#
    This macro returns the description of the ratecode id
#}

{% macro get_ratecode_id_description(RatecodeID) -%}

    case {{ RatecodeID }}
        when 1 then 'Standard rate'
        when 2 then 'JFK'
        when 3 then 'Newark'
        when 4 then 'Nassau or Westchester'
        when 5 then 'Negotiated fare'
        when 6 then 'Group ride'
    end

{%- endmacro %}