.. 
   Input file: fe/ips/udma/udma_aes/README.md

Register map
^^^^^^^^^^^^


Overview
""""""""

.. table:: 

    +------------------------------+------+-----+---------------------------+
    |             Name             |Offset|Width|        Description        |
    +==============================+======+=====+===========================+
    |:ref:`KEY0_0<udma_aes_KEY0_0>`|     0|   32|core 0 key 0               |
    +------------------------------+------+-----+---------------------------+
    |:ref:`KEY0_1<udma_aes_KEY0_1>`|     4|   32|core 0 key 1               |
    +------------------------------+------+-----+---------------------------+
    |:ref:`KEY0_2<udma_aes_KEY0_2>`|     8|   32|core 0 key 2               |
    +------------------------------+------+-----+---------------------------+
    |:ref:`KEY0_3<udma_aes_KEY0_3>`|    12|   32|core 0 key 3               |
    +------------------------------+------+-----+---------------------------+
    |:ref:`KEY0_4<udma_aes_KEY0_4>`|    16|   32|core 0 key 4               |
    +------------------------------+------+-----+---------------------------+
    |:ref:`KEY0_5<udma_aes_KEY0_5>`|    20|   32|core 0 key 5               |
    +------------------------------+------+-----+---------------------------+
    |:ref:`KEY0_6<udma_aes_KEY0_6>`|    24|   32|core 0 key 6               |
    +------------------------------+------+-----+---------------------------+
    |:ref:`KEY0_7<udma_aes_KEY0_7>`|    28|   32|core 0 key 7               |
    +------------------------------+------+-----+---------------------------+
    |:ref:`IV0_0<udma_aes_IV0_0>`  |    32|   32|core 0 IV 0                |
    +------------------------------+------+-----+---------------------------+
    |:ref:`IV0_1<udma_aes_IV0_1>`  |    36|   32|core 0 IV 1                |
    +------------------------------+------+-----+---------------------------+
    |:ref:`IV0_2<udma_aes_IV0_2>`  |    40|   32|core 0 IV 2                |
    +------------------------------+------+-----+---------------------------+
    |:ref:`IV0_3<udma_aes_IV0_3>`  |    44|   32|core 0 IV 3                |
    +------------------------------+------+-----+---------------------------+
    |:ref:`DEST<udma_aes_DEST>`    |    48|   32|RX TX destination channel  |
    +------------------------------+------+-----+---------------------------+
    |:ref:`SETUP<udma_aes_SETUP>`  |    52|   32|core setup                 |
    +------------------------------+------+-----+---------------------------+
    |:ref:`CFG<udma_aes_CFG>`      |    56|   32|AES data flow configuration|
    +------------------------------+------+-----+---------------------------+

.. _udma_aes_KEY0_0:

KEY0_0
""""""

core 0 key 0

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_KEY0_1:

KEY0_1
""""""

core 0 key 1

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_KEY0_2:

KEY0_2
""""""

core 0 key 2

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_KEY0_3:

KEY0_3
""""""

core 0 key 3

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_KEY0_4:

KEY0_4
""""""

core 0 key 4

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_KEY0_5:

KEY0_5
""""""

core 0 key 5

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_KEY0_6:

KEY0_6
""""""

core 0 key 6

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_KEY0_7:

KEY0_7
""""""

core 0 key 7

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_IV0_0:

IV0_0
"""""

core 0 IV 0

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_IV0_1:

IV0_1
"""""

core 0 IV 1

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_IV0_2:

IV0_2
"""""

core 0 IV 2

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_IV0_3:

IV0_3
"""""

core 0 IV 3

.. table:: 

    +-----+---+----+-----------+
    |Bit #|R/W|Name|Description|
    +=====+===+====+===========+
    +-----+---+----+-----------+

.. _udma_aes_DEST:

DEST
""""

RX TX destination channel

.. table:: 

    +-----+---+-------+--------------------------------------------------------------------+
    |Bit #|R/W| Name  |                            Description                             |
    +=====+===+=======+====================================================================+
    |7:0  |R/W|RX_DEST|Stream ID for the RX uDMA channel. Default is 0xFF(channel disabled)|
    +-----+---+-------+--------------------------------------------------------------------+
    |15:8 |R/W|TX_DEST|Stream ID for the TX uDMA channel. Default is 0xFF(channel disabled)|
    +-----+---+-------+--------------------------------------------------------------------+

.. _udma_aes_SETUP:

SETUP
"""""

core setup

.. table:: 

    +-----+---+---------+------------------------------------------+
    |Bit #|R/W|  Name   |               Description                |
    +=====+===+=========+==========================================+
    |    0|R  |KEY_INIT |Indicate the key configuration is finished|
    +-----+---+---------+------------------------------------------+
    |    1|R/W|KEY_TYPE |KEY type, 0 for 128B, 1 for 256B          |
    +-----+---+---------+------------------------------------------+
    |    2|R/W|ENC_DEC  |Operation type, 0 for DEC, 1 for ENC      |
    +-----+---+---------+------------------------------------------+
    |    3|R/W|ECB_CBC  |Enc_type, 0 for ECB, 1 for CBC            |
    +-----+---+---------+------------------------------------------+
    |    4|W  |BLOCK_RST|Block reset                               |
    +-----+---+---------+------------------------------------------+
    |    5|R/W|QK_KEY_EN|Use quiddikey key generation              |
    +-----+---+---------+------------------------------------------+
    |7:6  |-  |RESERVED |                                          |
    +-----+---+---------+------------------------------------------+
    |    8|W  |FIFO_CLR |Clean the fifo                            |
    +-----+---+---------+------------------------------------------+

.. _udma_aes_CFG:

CFG
"""

AES data flow configuration

.. table:: 

    +-----+---+----+---------------------------------------------------------------------------------------------------------+
    |Bit #|R/W|Name|                                               Description                                               |
    +=====+===+====+=========================================================================================================+
    |1:0  |R/W|MODE|Transfer MODE 2'b00: memory 2 memory 2'b01: Stream 2 memory 2'b10: Memory 2 Stream 2'b11: Stream 2 Stream|
    +-----+---+----+---------------------------------------------------------------------------------------------------------+
