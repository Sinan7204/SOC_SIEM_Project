const targetIds = [100501, 100502, 100503];

const currentId = parseInt(items[0].json?.body?.rule?.id);

if (currentId && targetIds.includes(currentId)) {
  return items; 
} else {
  return []; 
}