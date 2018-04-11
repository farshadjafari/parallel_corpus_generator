import csv

from models import Movie
corrupted_rows = [65, 82, 110, 197, 208, 221, 263, 277, 290, 296, 311, 336, 395, 402, 417, 420, 436, 461, 474, 490, 510, 514, 519, 520, 528, 529, 535, 546, 557, 611, 613, 622, 644, 645, 662, 712, 719, 720, 721, 729, 742, 748, 761, 773, 790, 812, 836, 844, 860, 873, 889, 898, 903, 916, 935, 943, 948, 950, 967, 993, 1014, 1026, 1044, 1045, 1048, 1056, 1057, 1060, 1070, 1096, 1103, 1105, 1139, 1169, 1193, 1194, 1195, 1217, 1219, 1251, 1269, 1289, 1293, 1303, 1324, 1331, 1333, 1337, 1347, 1350, 1354, 1360, 1362, 1394, 1399, 1401, 1402, 1403, 1417, 1430, 1437, 1450, 1465, 1475, 1481, 1484, 1489, 1516, 1547, 1548, 1574, 1585, 1589, 1595, 1597, 1615, 1616, 1617, 1619, 1625, 1626, 1636, 1653, 1657, 1662, 1665, 1671, 1679, 1680, 1686, 1703, 1704, 1718, 1721, 1741, 1758, 1761, 1765, 1767, 1769, 1772, 1777, 1779, 1797, 1798, 1812, 1824, 1839, 1843, 1866, 1898, 1899, 1900, 1906, 1912, 1923, 1938, 1944, 1977, 1981, 2022, 2023, 2027, 2053, 2075, 2080, 2082, 2091, 2106, 2159, 2223, 2259, 2260, 2288, 2289, 2328, 2347, 2348, 2352, 2370, 2386, 2390, 2394, 2407, 2434, 2464, 2504, 2506, 2509, 2517, 2529, 2537, 2546, 2583, 2587, 2594, 2603, 2611, 2621, 2636, 2651, 2660, 2704, 2710, 2713, 2721, 2728, 2775, 2781, 2805, 2825, 2855, 2857, 2881, 2908, 2981, 2982, 2996, 3004, 3016, 3018, 3022, 3038, 3051, 3061, 3085, 3088, 3093, 3097, 3105, 3133, 3156, 3162, 3167, 3176, 3189, 3190, 3191, 3192, 3199, 3202, 3204, 3208, 3213, 3216, 3221, 3237, 3240, 3241, 3254, 3272, 3291, 3292, 3302, 3311, 3312, 3313, 3321, 3323, 3330, 3335, 3353, 3357, 3359, 3361, 3376, 3381, 3395, 3411, 3412, 3419, 3421, 3426, 3431, 3434, 3436, 3441, 3443, 3450, 3457, 3459, 3464, 3465, 3468, 3470, 3474, 3475, 3477, 3480, 3495, 3499, 3509, 3521, 3522, 3523, 3532, 3536, 3538, 3563, 3572, 3585, 3591, 3605, 3606, 3609, 3612, 3618, 3620, 3625, 3626, 3644, 3658, 3673, 3677, 3679, 3684, 3685, 3693, 3695, 3705, 3718, 3719, 3721, 3724, 3726, 3730, 3734, 3739, 3740, 3752, 3753, 3762, 3767, 3772, 3776, 3783, 3789, 3791, 3794, 3805, 3806, 3824, 3830, 3833, 3834, 3848, 3857, 3863, 3870, 3883, 3900, 3901, 3903, 3913, 3923, 3924, 3925, 3932, 3942, 3965, 3968, 3973, 3998, 4003, 4011, 4013, 4023, 4024, 4033, 4037, 4043, 4044, 4061, 4068, 4081, 4091, 4111, 4117, 4148, 4159, 4161, 4165, 4171, 4181, 4188, 4205, 4215, 4216, 4221, 4227, 4254, 4261, 4265, 4266, 4279, 4281, 4298, 4307, 4311, 4328, 4333, 4339, 4367, 4376, 4377, 4388, 4389, 4397, 4403, 4411, 4414, 4415, 4422, 4425, 4427, 4431, 4436, 4441, 4444, 4451, 4460, 4470, 4495, 4503, 4505, 4513, 4516, 4518, 4530, 4539, 4553, 4554, 4555, 4557, 4566, 4571, 4592, 4606, 4608, 4613, 4616, 4634, 4640, 4672, 4680, 4684, 4687, 4689, 4698, 4718, 4734, 4735, 4741, 4745, 4749, 4755, 4756, 4763, 4764, 4765, 4772, 4786, 4792, 4795, 4810, 4815, 4820, 4848, 4864, 4884, 4888, 4889, 4891, 4892, 4893, 4896, 4904, 4910, 4918, 4922, 4932, 4935, 4947, 4951, 4952, 4953, 4955, 4956, 4961, 4965, 4966, 4970, 4973, 4981, 4996, 4999, 5011, 5015, 5021, 5025, 5028, 5033, 5034, 5056, 5060, 5064, 5070, 5079, 5089, 5096, 5098, 5103, 5104, 5113, 5116, 5124, 5127, 5134, 5141, 5146, 5153, 5160, 5161, 5166, 5179, 5182, 5183, 5185, 5186, 5187, 5191, 5194, 5201, 5203, 5204, 5206, 5212, 5215, 5218, 5221, 5229, 5231, 5232, 5238, 5243, 5244, 5254, 5260, 5266, 5268, 5269, 5271, 5274, 5275, 5289, 5290, 5293, 5295, 5300, 5305, 5308, 5314, 5317, 5324, 5329, 5333, 5338, 5345, 5349, 5350, 5352, 5357, 5360, 5367, 5368, 5377, 5380, 5382, 5386, 5403, 5424, 5425, 5428, 5429, 5431, 5434, 5439, 5440, 5444, 5445, 5446, 5451, 5454, 5455, 5459, 5460, 5471, 5473, 5475, 5479, 5480, 5491, 5498, 5499, 5502, 5504, 5508, 5509, 5510, 5513, 5522, 5526, 5527, 5529, 5532, 5539, 5541, 5543, 5547, 5549, 5555, 5557, 5558, 5559, 5560, 5561, 5562, 5564, 5565, 5566, 5567, 5572, 5582, 5585, 5589, 5590, 5599, 5603, 5604, 5605, 5610, 5614, 5615, 5616, 5620, 5631, 5634, 5639, 5640, 5645, 5650, 5651, 5652, 5654, 5657, 5658, 5660, 5668, 5670, 5672, 5676, 5682, 5686, 5687, 5688, 5690, 5693, 5694, 5697, 5699, 5701, 5702, 5706, 5707, 5708, 5709, 5710, 5712, 5716, 5718, 5719, 5720, 5724, 5727, 5728, 5730, 5731, 5734, 5736, 5737, 5740, 5746, 5748, 5750, 5751, 5755, 5758, 5763, 5764, 5765, 5766, 5768, 5769, 5773, 5776, 5781, 5782, 5783, 5789, 5790, 5793, 5794, 5795, 5801, 5807, 5812, 5813, 5817, 5818, 5819, 5828, 5829, 5832, 5839, 5840, 5841, 5842, 5843, 5850, 5851, 5853, 5858, 5864, 5865, 5866, 5867, 5871, 5874, 5875, 5876, 5877, 5878, 5880, 5885, 5892, 5893, 5896, 5897, 5898, 5900, 5904, 5909, 5910, 5913, 5914, 5915, 5916, 5917, 5921, 5927, 5928, 5932, 5934, 5936, 5938, 5939, 5941, 5945, 5951, 5953, 5954, 5956, 5957, 5959, 5962, 5963, 5964, 5965, 5966, 5969, 5970, 5971, 5973, 5974, 5979, 5980, 5982, 5983, 5985, 5988, 5989, 5991, 5995, 5996, 5997, 5998, 5999, 6001, 6007, 6008, 6011, 6024, 6025, 6026, 6027, 6028, 6030, 6032, 6033, 6036, 6037, 6038, 6039, 6040, 6042, 6043, 6044, 6046, 6047, 6048, 6050, 6051, 6052, 6053, 6054, 6056, 6057, 6058, 6059, 6060, 6061, 6062, 6063, 6065, 6069, 6070, 6072, 6073, 6074, 6075, 6078, 6080, 6084, 6085, 6086, 6087, 6088, 6089, 6090, 6093, 6094, 6095, 6096, 6097, 6098, 6101, 6102, 6104, 6106, 6107, 6108, 6109, 6110, 6111, 6114, 6118, 6120, 6122, 6128, 6130, 6131, 6134, 6135, 6137, 6139, 6141, 6144, 6145, 6146, 6147, 6148, 6153, 6156, 6157, 6158, 6160, 6161, 6163, 6164, 6166, 6167, 6169, 6172, 6173, 6179, 6183, 6184, 6185, 6186, 6187, 6188, 6189, 6191, 6192, 6196, 6197, 6201, 6205, 6206, 6208, 6209, 6215, 6217, 6218, 6221, 6222, 6225, 6230, 6232, 6233, 6235, 6236, 6237, 6240, 6242, 6243, 6244, 6245, 6246, 6251, 6254, 6255, 6259, 6260, 6261, 6263, 6265, 6267, 6268, 6270, 6271, 6272, 6273, 6274, 6275, 6276, 6277, 6278, 6279, 6280, 6282, 6283, 6284, 6285, 6287, 6288, 6294, 6295, 6296, 6299, 6300, 6301, 6302, 6303, 6305, 6306, 6308, 6310, 6311, 6312, 6313, 6315, 6318, 6320, 6321, 6322, 6324, 6326, 6327, 6328, 6330, 6331, 6332, 6333, 6336, 6337, 6338, 6341, 6347, 6349, 6351, 6353, 6355, 6356, 6357, 6358, 6359, 6361, 6365, 6367, 6369, 6371, 6372, 6375, 6376, 6377, 6379, 6381, 6383, 6386, 6387, 6391, 6393, 6394, 6395, 6396, 6398, 6403, 6404, 6414, 6416, 6417, 6419, 6421, 6424, 6425, 6426, 6427, 6428, 6431, 6437, 6439, 6440, 6441, 6443, 6445, 6447, 6448, 6450, 6451, 6453, 6456, 6458, 6461, 6463, 6464, 6465, 6466, 6470, 6471, 6472, 6473, 6475, 6476, 6477, 6479, 6482, 6483, 6485, 6489, 6493, 6495, 6496, 6497, 6499, 6501, 6503, 6505, 6506, 6507, 6511, 6513, 6516, 6517, 6518, 6521, 6522, 6523, 6524, 6526, 6528, 6529, 6531, 6533, 6534, 6537, 6538, 6539, 6540, 6542, 6543, 6545, 6546, 6548, 6549, 6550, 6551, 6553, 6554, 6555, 6556, 6557, 6559, 6560, 6561, 6564, 6565, 6566, 6567, 6569, 6570, 6571, 6573, 6574, 6575, 6579, 6580, 6581, 6584, 6586, 6588, 6589, 6593, 6594, 6595, 6596, 6597, 6599, 6600, 6601, 6602, 6604, 6605, 6606, 6607, 6608, 6609, 6613, 6614, 6615, 6616, 6617, 6623, 6624, 6625, 6626, 6627, 6629, 6630, 6631, 6632, 6633, 6634, 6635, 6636, 6637, 6640, 6641, 6646, 6647, 6650, 6651, 6652, 6653, 6654, 6657, 6659, 6660, 6662, 6663, 6664, 6665, 6668, 6669, 6670, 6672, 6673, 6674, 6675, 6677, 6678, 6679, 6680, 6681, 6682, 6685, 6688, 6689, 6690, 6691, 6692, 6713, 6726, 6729, 6739, 6740, 6742, 6751, 6762, 6794, 6810, 6816, 6828, 6850, 6852, 6853, 6888, 6889, 6896, 6897, 6903, 6913, 6914, 6916, 6938, 6947, 6968, 6978, 6981, 6982, 6983, 6984, 7009, 7020, 7021, 7023, 7030, 7033, 7035, 7040, 7056, 7068, 7076, 7081, 7086, 7099, 7100, 7112, 7113, 7136, 7138, 7140, 7145, 7157, 7163, 7167, 7169, 7173, 7179, 7181, 7196, 7210, 7215, 7216, 7221, 7231, 7235, 7237, 7238, 7261, 7271, 7282, 7294, 7298, 7303, 7311, 7316, 7318, 7324, 7333, 7340, 7343, 7345, 7346, 7358, 7367, 7374, 7375, 7379, 7383, 7391, 7394, 7397, 7398, 7401, 7402, 7410, 7415, 7416, 7418, 7419, 7423, 7433, 7438, 7439, 7442, 7455, 7461, 7471, 7478, 7493, 7495, 7498, 7532, 7533, 7540, 7547, 7550, 7553, 7557, 7570, 7571, 7583, 7584, 7585, 7595, 7603, 7607, 7609, 7615, 7617, 7621, 7626, 7630, 7631, 7635, 7638, 7641, 7645, 7647, 7648, 7653, 7659, 7665, 7669, 7672, 7675, 7676, 7678, 7687, 7689, 7696, 7702, 7703, 7704, 7705, 7711, 7716, 7720, 7721, 7726, 7737, 7744, 7753, 7755, 7757, 7766, 7770, 7772, 7778, 7779, 7780, 7781, 7785, 7786, 7787, 7788, 7801, 7802, 7806, 7807, 7810, 7823, 7834, 7838, 7846, 7847, 7849, 7850, 7851, 7856, 7860, 7863, 7873, 7879, 7883, 7885, 7887, 7898, 7899, 7909, 7912, 7915, 7923, 7925, 7927, 7930, 7931, 7934, 7935, 7936, 7941, 7944, 7954, 7958, 7960, 7961, 7962, 7971, 7972, 7979, 7980, 7983, 7988, 7989, 7996, 7998, 8004, 8007, 8008, 8018, 8019, 8020, 8021, 8022, 8023, 8025, 8027, 8028, 8032, 8036, 8041, 8051, 8054, 8056, 8058, 8061, 8066, 8069, 8071, 8075, 8078, 8085, 8091, 8102, 8103, 8104, 8106, 8108, 8114, 8117, 8118, 8122, 8125, 8128, 8133, 8135, 8137, 8141, 8144, 8145, 8151, 8155, 8156, 8159, 8162, 8178, 8187, 8190, 8193, 8197, 8201, 8204, 8213, 8218, 8220, 8227, 8231, 8240, 8243, 8245, 8246, 8249, 8254, 8255, 8256, 8259, 8262, 8263, 8272, 8274, 8279, 8280, 8281, 8282, 8288, 8297, 8300, 8305, 8309, 8310, 8311, 8317, 8318, 8329, 8336, 8340, 8342, 8344, 8348, 8349, 8350, 8351, 8355, 8359, 8361, 8362, 8363, 8366, 8369, 8374, 8377, 8383, 8387, 8389, 8391, 8397, 8399, 8401, 8406, 8410, 8411, 8417, 8418, 8419, 8423, 8428, 8431, 8433, 8437, 8442, 8443, 8444, 8445, 8447, 8448, 8450, 8451, 8456, 8457, 8459, 8463, 8464, 8465, 8468, 8472, 8473, 8476, 8477, 8478, 8481, 8483, 8489, 8490, 8492, 8499, 8509, 8510, 8513, 8517, 8519, 8521, 8522, 8523, 8527, 8529, 8530, 8531, 8535, 8536, 8537, 8539, 8540, 8541, 8542, 8543, 8544, 8548, 8552, 8555, 8557, 8558, 8564, 8566, 8571, 8572, 8578, 8580, 8583, 8585, 8588, 8589, 8590, 8591, 8592, 8593, 8594, 8599, 8607, 8608, 8614, 8618, 8619, 8621, 8624, 8626, 8631, 8634, 8644, 8647, 8651, 8653, 8656, 8657, 8659, 8665, 8668, 8673, 8678, 8683, 8684, 8694, 8696, 8698, 8701, 8702, 8703, 8705, 8708, 8709, 8713, 8715, 8716, 8717, 8720, 8721, 8723, 8724, 8727, 8731, 8733, 8734, 8735, 8736, 8740, 8741, 8747, 8748, 8749, 8754, 8761, 8763, 8764, 8767, 8778, 8779, 8781, 8782, 8785, 8790, 8791, 8793, 8796, 8798, 8801, 8802, 8803, 8804, 8805, 8806, 8809, 8810, 8811, 8813, 8814, 8817, 8820, 8821, 8822, 8824, 8826, 8827, 8828, 8829, 8830, 8831, 8832, 8835, 8836, 8837, 8838, 8842, 8843, 8844, 8845, 8846, 8850, 8855, 8856, 8859, 8863, 8864, 8865, 8871, 8873, 8878, 8880, 8881, 8884, 8887, 8888, 8892, 8893, 8895, 8900, 8902, 8903, 8904, 8908, 8909, 8911, 8912, 8914, 8915, 8918, 8920, 8922, 8923, 8926, 8930, 8931, 8941, 8944, 8945, 8946, 8947, 8948, 8952, 8957, 8959, 8960, 8961, 8964, 8965, 8974, 8975, 8977, 8979, 8981, 8982, 8983, 8987, 8988, 8989, 8992, 8995, 8996, 8997, 9000, 9001, 9002, 9004, 9010, 9012, 9014, 9015, 9016, 9018, 9020, 9023, 9024, 9030, 9032, 9033, 9034, 9035, 9037, 9038, 9040, 9042, 9043, 9044, 9047, 9052, 9053, 9054, 9056, 9059, 9061, 9064, 9067, 9068, 9070, 9076, 9078, 9079, 9080, 9082, 9084, 9089, 9092, 9096, 9097, 9098, 9099, 9101, 9102, 9106, 9107, 9110, 9111, 9113, 9114, 9116, 9117, 9119, 9120, 9125, 9127, 9128, 9131, 9133, 9134, 9136, 9138, 9139, 9140, 9142, 9147, 9148, 9150, 9151, 9152, 9154, 9155, 9157, 9159, 9160, 9161, 9165, 9168, 9169, 9172, 9176, 9177, 9178, 9181, 9182, 9183, 9184, 9185, 9187, 9188, 9193, 9198, 9200, 9201, 9202, 9205, 9208, 9209, 9211, 9212, 9214, 9215, 9216, 9217, 9218, 9219, 9220, 9221, 9222, 9223, 9224, 9227, 9229, 9232, 9233, 9243, 9249, 9250, 9252, 9254, 9256, 9258, 9260, 9262, 9263, 9267, 9268, 9271, 9272, 9273, 9278, 9280, 9282, 9284, 9291, 9292, 9297, 9300, 9304, 9306, 9308, 9309, 9312, 9313, 9317, 9318, 9320, 9325, 9327, 9331, 9332, 9335, 9337, 9339, 9340, 9341, 9344, 9346, 9348, 9350, 9351, 9353, 9356, 9357, 9360, 9365, 9368, 9371, 9372, 9377, 9378, 9379, 9380, 9382, 9384, 9386, 9388, 9389, 9392, 9393, 9394, 9395, 9399, 9401, 9402, 9403, 9406, 9407, 9408, 9411, 9412, 9414, 9415, 9420, 9421, 9423, 9425, 9426, 9427, 9428, 9429, 9430, 9432, 9433, 9435, 9437, 9438, 9440, 9441, 9442, 9445, 9446, 9450, 9452, 9456, 9457, 9458, 9459, 9460, 9464, 9467, 9469, 9470, 9474, 9475, 9477, 9479, 9481, 9485, 9486, 9488, 9491, 9493, 9494, 9495, 9497, 9498, 9499, 9502, 9503, 9504, 9505, 9508, 9510, 9512, 9513, 9515, 9516, 9517, 9518, 9519, 9520, 9521, 9522, 9523, 9526, 9527, 9530, 9531, 9533, 9535, 9536, 9537, 9539, 9540, 9541, 9544, 9545, 9546, 9549, 9550, 9551, 9552, 9553, 9554, 9555, 9556, 9557, 9558, 9559, 9560, 9561, 9563, 9564, 9574, 9575, 9577, 9596, 9663, 9670, 9689, 9699, 9710, 9712, 9741, 9757, 9758, 9766, 9775, 9804, 9825, 9833, 9836, 9843, 9850, 9853, 9859, 9889, 9896, 9937, 9949, 9956, 9978, 9979, 10000, 10001, 10014, 10022, 10031, 10050, 10058, 10060, 10085, 10095, 10098, 10101, 10117, 10120, 10148, 10161, 10167, 10183, 10198, 10203, 10217, 10221, 10223, 10233, 10242, 10256, 10264, 10293, 10295, 10322, 10330, 10333, 10341, 10343, 10350, 10377, 10413, 10415, 10428, 10429, 10462, 10476, 10477, 10504, 10515, 10532, 10535, 10538, 10544, 10548, 10581, 10587, 10595, 10597, 10601, 10648, 10659, 10687, 10697, 10732, 10772, 10778, 10787, 10799, 10803, 10805, 10838, 10861, 10869, 10871, 10877, 10880, 10883, 10901, 10904, 10929, 10933, 10951, 10992, 10993, 11022, 11049, 11066, 11069, 11083, 11105, 11109, 11111, 11122, 11127, 11128, 11153, 11194, 11195, 11209, 11222, 11225, 11253, 11277, 11289, 11357, 11364, 11389, 11390, 11420, 11430, 11432, 11433, 11441, 11442, 11468, 11474, 11479, 11498, 11512, 11521, 11522, 11530, 11533, 11552, 11554, 11566, 11589, 11606, 11609, 11638, 11640, 11654, 11688, 11720, 11752, 11766, 11767, 11775, 11796, 11808, 11848, 11881, 11883, 11889, 11914, 11916, 11928, 11955, 12020, 12030, 12035, 12036, 12037, 12039, 12046, 12049, 12054, 12079, 12080, 12107, 12157, 12159, 12179, 12183, 12186, 12187, 12216, 12222, 12223, 12226, 12232, 12246, 12250, 12255, 12256, 12258, 12263, 12268, 12273, 12320, 12354, 12360, 12368, 12372, 12375, 12377, 12392, 12393, 12394, 12396, 12397, 12402, 12406, 12438, 12440, 12458, 12460, 12466, 12485, 12488, 12505, 12515, 12517, 12522, 12527, 12531, 12532, 12541, 12544, 12545, 12554, 12567, 12572, 12579, 12587, 12588, 12594, 12596, 12605, 12608, 12613, 12619, 12641, 12650, 12655, 12656, 12659, 12660, 12663, 12664, 12668, 12670, 12679, 12680, 12682, 12685, 12690, 12696, 12700, 12714, 12740, 12755, 12764, 12768, 12770, 12771, 12775, 12776, 12786, 12791, 12799, 12801, 12810, 12811, 12822, 12826, 12830, 12839, 12848, 12850, 12857, 12861, 12863, 12876, 12879, 12881, 12886, 12888, 12891, 12899, 12902, 12908, 12909, 12912, 12913, 12925, 12929, 12936, 12948, 12949, 12950, 12954, 12957, 12959, 12963, 12970, 12972, 12981, 13012, 13018, 13023, 13027, 13045, 13046, 13051, 13052, 13055, 13060, 13065, 13069, 13083, 13101, 13105, 13114, 13115, 13119, 13120, 13122, 13127, 13131, 13135, 13138, 13143, 13147, 13148, 13155, 13157, 13158, 13159, 13160, 13163, 13166, 13169, 13170, 13175, 13180, 13185, 13190, 13191, 13192, 13203, 13208, 13230, 13239, 13246, 13248, 13256, 13258, 13260, 13261, 13263, 13265, 13269, 13271, 13295, 13311, 13313, 13315, 13319, 13322, 13351, 13357, 13358, 13361, 13363, 13364, 13370, 13373, 13374, 13376, 13383, 13393, 13400, 13402, 13406, 13411, 13419, 13421, 13426, 13429, 13432, 13435, 13449, 13451, 13454, 13456, 13467, 13473, 13475, 13476, 13481, 13485, 13490, 13493, 13494, 13505, 13528, 13529, 13539, 13544, 13548, 13555, 13556, 13564, 13568, 13571, 13572, 13578, 13582, 13583, 13594, 13599, 13600, 13616, 13628, 13631, 13636, 13643, 13648, 13650, 13651, 13654, 13659, 13662, 13666, 13672, 13675, 13676, 13677, 13680, 13687, 13690, 13693, 13706, 13709, 13710, 13713, 13720, 13725, 13726, 13728, 13729, 13730, 13749, 13753, 13758, 13764, 13765, 13769, 13774, 13775, 13779, 13803, 13805, 13821, 13825, 13826, 13827, 13831, 13834, 13836, 13840, 13864, 13869, 13882, 13889, 13895, 13897, 13902, 13906, 13909, 13914, 13923, 13928, 13947, 13949, 13960, 13977, 13983, 13999, 14014, 14019, 14021, 14023, 14025, 14031, 14039, 14041, 14065, 14078, 14089, 14090, 14094, 14100, 14102, 14109, 14118, 14123, 14126, 14135, 14142, 14147, 14152, 14165, 14172, 14173, 14175, 14192, 14194, 14195, 14199, 14215, 14226, 14227, 14228, 14235, 14236, 14242, 14244, 14248, 14251, 14253, 14259, 14260, 14269, 14274, 14276, 14298, 14299, 14306, 14312, 14313, 14317, 14319, 14321, 14341, 14345, 14348, 14353, 14355, 14367, 14380, 14391, 14412, 14416, 14423, 14433, 14435, 14440, 14443, 14448, 14450, 14455, 14458, 14463, 14465, 14474, 14477, 14478, 14486, 14499, 14503, 14506, 14508, 14509, 14513, 14521, 14525, 14551, 14554, 14557, 14559, 14562, 14564, 14571, 14584, 14593, 14614, 14615, 14622, 14630, 14631, 14633, 14634, 14635, 14636, 14637, 14641, 14643, 14648, 14651, 14655, 14662, 14663, 14669, 14686, 14687, 14701, 14709, 14711, 14714, 14715, 14716, 14739, 14760]
with open('imdb.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in reader:
        if count == 0:
            count += 1
            continue
        try:
            movie = Movie(title=row[2], words_in_title=row[3], movie_type=row[9], rate=float(row[5]), duration=int(row[7]),
                          year=row[8])
            movie.save()
        except:
            print '#####################error', count
        count += 1


    #
    # rows = list(reader)
    # count = 0
    # for corrupted_row in corrupted_rows:
    #     print rows[corrupted_row]
    #     count += 1
    #     if count > 10: break