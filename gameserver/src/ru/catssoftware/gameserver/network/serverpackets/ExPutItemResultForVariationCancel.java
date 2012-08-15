/*
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation, either version 3 of the License, or (at your option) any later
 * version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program. If not, see <http://www.gnu.org/licenses/>.
 */
package ru.catssoftware.gameserver.network.serverpackets;

/**
 * Format: (ch)ddd
 *
 */
public class ExPutItemResultForVariationCancel extends L2GameServerPacket
{
	private static final String	_S__FE_56_EXCONFIRMCANCELITEM	= "[S] FE:56 ExConfirmCancelItem";

	private int					_itemObjId;
	private int					_price;

	public ExPutItemResultForVariationCancel(int itemObjId, int price)
	{
		_itemObjId = itemObjId;
		_price = price;
	}

	/**
	 * @see ru.catssoftware.gameserver.network.serverpackets.ServerBasePacket#writeImpl()
	 */
	@Override
	protected void writeImpl()
	{
		writeC(0xFE);
		writeH(0x56);
		writeD(0x40A97712);
		writeD(_itemObjId);
		writeD(0x27);
		writeD(0x2006);
		writeQ(_price);
		writeD(0x01);
	}

	/**
	 * @see ru.catssoftware.gameserver.BasePacket#getType()
	 */
	@Override
	public String getType()
	{
		return _S__FE_56_EXCONFIRMCANCELITEM;
	}

}