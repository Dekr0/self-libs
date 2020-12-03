import huffman, bitio
import pickle


def read_tree(tree_stream):
    """Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    """

    tree = pickle.load(tree_stream)

    return tree
    # pass


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    if isinstance(tree, huffman.TreeLeaf):
        l_value = tree.getValue()
        if l_value != None:
            return l_value, True
        return l_value, False

    bit = bitreader.readbit()

    if bit:
        r_subtree = tree.getRight()
        return decode_byte(r_subtree, bitreader)

    l_subtree = tree.getLeft()
    return decode_byte(l_subtree, bitreader)

    # pass


def decompress(compressed, uncompressed):
    """First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    """

    tree = read_tree(compressed)

    reader = bitio.BitReader(compressed)
    writer = bitio.BitWriter(uncompressed)
    EOF = False

    while not EOF:
        l_value, c_EOF = decode_byte(tree, reader)

        if not c_EOF:
            EOF = True

        try:
                writer.writebits(l_value, 8)
        except:
            writer.flush()
            uncompressed.flush()

    writer.flush()
    uncompressed.flush()
    # pass


def write_tree(tree, tree_stream):
    """Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    """
    pickle.dump(tree, tree_stream)

    return
    # pass


def compress(tree, uncompressed, compressed):
    """First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    """

    write_tree(tree, compressed)

    encoding_table = huffman.make_encoding_table(tree)
    reader = bitio.BitReader(uncompressed)
    writer = bitio.BitWriter(compressed)

    total_bits = 0
    EOF = False

    while not EOF:
        try:
            byte = reader.readbits(8)
            edges = encoding_table[byte]

            for edge in edges:
                try:
                    writer.writebit(edge)
                    total_bits += 1
                except:
                    writer.flush()
                    compressed.flush()

        except EOFError:
            EOF = True

            eof_edges = encoding_table[None]
            for eof_edge in eof_edges:
                try:
                    writer.writebit(eof_edge)
                    total_bits += 1
                except:
                    writer.flush()
                    compressed.flush()

            remain = total_bits % 8
            if remain > 0:
                for i in range(remain):
                    try:
                        writer.writebit(False)
                    except:
                        writer.flush()
                        compressed.flush()

    writer.flush()
    compressed.flush()
    # pass
