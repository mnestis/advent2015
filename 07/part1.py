#!/usr/bin/python

import re
import numpy

re_two_input_gate = re.compile("([\d\w]+) (AND|OR) ([\d\w]+)$")
re_shift_gate = re.compile("([\d\w]+) (LSHIFT|RSHIFT) (\d+)$")
re_one_input_gate = re.compile("NOT ([\d\w]+)$")
re_wire = re.compile("([\d\w]+)$")

def emulate_circuit(input_string, node_to_return):
    
    nodes = {}

    split = re.compile("([\w\d\s]+) -> (\w+)")

    for row in input_string.split("\n"):
        if row == "":
            continue

        split_values = split.match(row).groups()
        nodes[split_values[1]] = split_values[0]

    return evaluate_node(node_to_return, nodes)

def evaluate_node(node_id, nodes):
    
    if re.match("\d+", node_id) is not None:
        return numpy.uint16(node_id)

    node_spec = nodes[node_id]
    
    two_input_gate = re_two_input_gate.match(node_spec)
    shift_gate = re_shift_gate.match(node_spec)
    one_input_gate = re_one_input_gate.match(node_spec)
    wire = re_wire.match(node_spec)

    if wire is not None:
        output = evaluate_node(wire.groups()[0], nodes)
        nodes[node_id] = str(output)
        return output

    elif two_input_gate is not None:
        re_groups = two_input_gate.groups()

        node_a = evaluate_node(re_groups[0], nodes)
        node_b = evaluate_node(re_groups[2], nodes)
        
        if re_groups[1] == "AND":
            output = numpy.bitwise_and(node_a, node_b)
            nodes[node_id] = str(output)
            return output
        elif re_groups[1] == "OR":
            output = numpy.bitwise_or(node_a, node_b)
            nodes[node_id] = str(output)
            return output
        else:
            raise Exception("AND OR broken")

    elif shift_gate is not None:
        re_groups = shift_gate.groups()
        node_a = evaluate_node(re_groups[0], nodes)

        if re_groups[1] == "LSHIFT":
            output = numpy.left_shift(node_a, int(re_groups[2]))
            nodes[node_id] = str(output)
            return output
        elif re_groups[1] == "RSHIFT":
            output = numpy.right_shift(node_a, int(re_groups[2]))
            nodes[node_id] = str(output)
            return output
        else:
            raise Exception("SHIFT broken")

    elif one_input_gate is not None:
        node_a = evaluate_node(one_input_gate.groups()[0], nodes)
        output = ~node_a
        nodes[node_id] = str(output)
        return output

    else:
        raise Exception("Unrecognised command...")

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print emulate_circuit(input_string, "a")
